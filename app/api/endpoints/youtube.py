from fastapi import APIRouter

from app.core.youtube_service import YouTubeService

router = APIRouter()


@router.get("/youtube")
async def youtube_endpoint():
    # Implement YouTube endpoint
    pass
