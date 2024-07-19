from fastapi import FastAPI

from app.interface.api.notion_endpoint import router as notion_router

app = FastAPI()


app.include_router(notion_router, prefix="/api", tags=["notion"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Notion API Integration"}
