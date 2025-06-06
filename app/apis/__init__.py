from fastapi import APIRouter
from .routes import (
    auth_router,
    users_router,
)

api_router = APIRouter(prefix="/api", tags=["API"])

api_router.include_router(auth_router)
api_router.include_router(users_router)
