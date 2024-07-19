from app.domain.interfaces.repositories import notion_repository_interface
from app.domain.models.notion_models import NotionDatabase
from app.domain.services.notion_domain_service import NotionDomainService


class NotionApplicationService:
    def __init__(self, repository: notion_repository_interface, domain_service: NotionDomainService):
        self.repository = repository
        self.domain_service = domain_service

    async def get_processed_database(self, database_id: str) -> NotionDatabase:
        database = await self.repository.get_database(database_id)
        processed_database = self.domain_service.process_database(database)
        return processed_database
