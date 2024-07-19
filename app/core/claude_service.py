import anthropic
from app.core.config import settings


class ClaudeService:
    def __init__(self):
        self.client = anthropic.Client(api_key=settings.CLAUDE_API_KEY)

    # Add Claude API methods here
