from fastapi import APIRouter
from .room import router as room_router
from .lesson import router as lesson_router

router = APIRouter(
    prefix='/v1'
)

router.include_router(room_router)
router.include_router(lesson_router)
