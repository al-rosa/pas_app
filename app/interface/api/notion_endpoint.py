from fastapi import APIRouter, Depends

from app.application.services.notion_service import NotionApplicationService
from app.domain.models.notion_models import NotionDatabase
from app.domain.services.notion_domain_service import NotionDomainService
from app.infrastructure.repositories.notion_repository import NotionRepository

router = APIRouter()


def get_notion_service():
    repository = NotionRepository()
    domain_service = NotionDomainService()
    return NotionApplicationService(repository, domain_service)


@router.get("/notion/database/{database_id}", response_model=NotionDatabase)
async def get_notion_database(database_id: str, service: NotionApplicationService = Depends(get_notion_service)):
    return await service.get_processed_database(database_id)
