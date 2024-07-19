from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.models.notion_models import NotionDatabase, NotionPage


class NotionRepositoryInterface(ABC):
    @abstractmethod
    async def get_database(self, database_id: str) -> NotionDatabase:
        """指定されたIDのNotionデータベースを取得する"""
        pass

    @abstractmethod
    async def get_pages(self, database_id: str, filter_params: Optional[dict] = None) -> List[NotionPage]:
        """データベース内のページを取得する。オプションでフィルターを適用可能"""
        pass

    @abstractmethod
    async def create_page(self, database_id: str, page_data: dict) -> NotionPage:
        """新しいページをデータベースに作成する"""
        pass

    @abstractmethod
    async def update_page(self, page_id: str, page_data: dict) -> NotionPage:
        """既存のページを更新する"""
        pass

    @abstractmethod
    async def delete_page(self, page_id: str) -> None:
        """ページを削除する（アーカイブする）"""
        pass

    @abstractmethod
    async def search_pages(self, query: str) -> List[NotionPage]:
        """ページを検索する"""
        pass
