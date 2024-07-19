import requests

import core.config as settings


class NotionExternalImpl:
    def __init__(self):
        self.token = settings.NOTION_TOKEN
        self.version = settings.NOTION_VERSION
        self.base_url = 'https://api.notion.com/v1/databases/'

    def query_database(self, database_id: str):
        url = f"{self.base_url}{database_id}/query"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Notion-Version': self.version
        }
        response = requests.post(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
