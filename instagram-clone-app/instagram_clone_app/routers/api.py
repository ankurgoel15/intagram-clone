from fastapi import APIRouter
from .endpoints import user_router

api_router = APIRouter()

api_router.include_router(user_router.router, prefix="/user", tags=["User"])
