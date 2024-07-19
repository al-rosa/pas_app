from fastapi import FastAPI

from app.api.endpoints import claude, notion, youtube

app = FastAPI()

app.include_router(youtube.router)
app.include_router(notion.router)
app.include_router(claude.router)
