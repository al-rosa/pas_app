from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    YOUTUBE_API_KEY: str
    NOTION_API_KEY: str
    CLAUDE_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
