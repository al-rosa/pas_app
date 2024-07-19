from typing import List, Optional

from notion_client import AsyncClient

from app.core.config import settings
from app.core.exceptions import NotionAPIError
from app.domain.interfaces.repositories.notion_repository_interface import \
    NotionRepositoryInterface
from app.domain.models.notion_models import NotionDatabase, NotionPage


class NotionRepository(NotionRepositoryInterface):
    def __init__(self):
        self.client = AsyncClient(auth=settings.NOTION_API_KEY)

    async def get_database(self, database_id: str) -> NotionDatabase:
        try:
            response = await self.client.databases.retrieve(database_id=database_id)
            return NotionDatabase(
                id=response['id'],
                title=response['title'][0]['plain_text'] if response['title'] else '',
                description=response.get('description', [{}])[
                    0].get('plain_text', '')
            )
        except Exception as e:
            raise NotionAPIError(f"Failed to retrieve database: {str(e)}")

    async def get_pages(self, database_id: str, filter_params: Optional[dict] = None) -> List[NotionPage]:
        try:
            response = await self.client.databases.query(
                database_id=database_id,
                filter=filter_params
            )
            return [self._parse_page(page) for page in response['results']]
        except Exception as e:
            raise NotionAPIError(f"Failed to retrieve pages: {str(e)}")

    async def create_page(self, database_id: str, page_data: dict) -> NotionPage:
        try:
            response = await self.client.pages.create(
                parent={"database_id": database_id},
                properties=page_data
            )
            return self._parse_page(response)
        except Exception as e:
            raise NotionAPIError(f"Failed to create page: {str(e)}")

    async def update_page(self, page_id: str, page_data: dict) -> NotionPage:
        try:
            response = await self.client.pages.update(
                page_id=page_id,
                properties=page_data
            )
            return self._parse_page(response)
        except Exception as e:
            raise NotionAPIError(f"Failed to update page: {str(e)}")

    async def delete_page(self, page_id: str) -> None:
        try:
            await self.client.pages.update(
                page_id=page_id,
                archived=True
            )
        except Exception as e:
            raise NotionAPIError(f"Failed to delete page: {str(e)}")

    async def search_pages(self, query: str) -> List[NotionPage]:
        try:
            response = await self.client.search(query=query)
            return [self._parse_page(page) for page in response['results'] if page['object'] == 'page']
        except Exception as e:
            raise NotionAPIError(f"Failed to search pages: {str(e)}")

    def _parse_page(self, page_data: dict) -> NotionPage:
        return NotionPage(
            id=page_data['id'],
            title=page_data['properties'].get('Name', {}).get(
                'title', [{}])[0].get('plain_text', ''),
            url=page_data.get('url', ''),
            content=self._extract_content(page_data)
        )

    def _extract_content(self, page_data: dict) -> str:
        # This is a simplified content extraction.
        # You may need to implement a more sophisticated method depending on your needs.
        return page_data.get('plain_text', '')
