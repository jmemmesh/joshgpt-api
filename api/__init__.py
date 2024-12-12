from fastapi import APIRouter
from .api import router
from .health import router as health_router

api_router = APIRouter(prefix="/joshgpt")

api_router.include_router(router)
api_router.include_router(health_router)