

from ..models.notion_models import NotionDatabase


class NotionDomainService:
    def process_database(self, database: NotionDatabase) -> NotionDatabase:
        # ここでドメイン固有のロジックを適用できます
        # 例: ページのフィルタリング、データの変換など
        return database
