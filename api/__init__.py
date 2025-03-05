from fastapi import APIRouter

from backend.core.config import settings
from backend.api.routes import dummy

api_router = APIRouter()
api_router.include_router(dummy.router)


if settings.ENVIRONMENT == "local":
    pass