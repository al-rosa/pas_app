from notion_client import Client
from app.core.config import settings


class NotionService:
    def __init__(self):
        self.notion = Client(auth=settings.NOTION_API_KEY)

    # Add Notion API methods here
