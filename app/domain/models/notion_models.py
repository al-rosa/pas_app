from typing import List

from pydantic import BaseModel


class NotionPage(BaseModel):
    id: str
    title: str
    content: str


class NotionDatabase(BaseModel):
    id: str
    pages: List[NotionPage]
