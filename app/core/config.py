from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    NOTION_API_KEY: str
    NOTION_API_VERSION: str

    class Config:
        env_file = ".env"


settings = Settings()
