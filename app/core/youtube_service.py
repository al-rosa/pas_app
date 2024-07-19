from googleapiclient.discovery import build
from app.core.config import settings


class YouTubeService:
    def __init__(self):
        self.youtube = build(
            'youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)

    # Add YouTube API methods here
