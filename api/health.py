from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["health"])
async def app_health():
    return {"status": "OK"}