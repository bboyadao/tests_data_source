from fastapi import APIRouter
from app.api import crawl_routers


app_routers: APIRouter = APIRouter()
app_routers.include_router(crawl_routers, prefix="/crawl", tags=["CRAWL"])
