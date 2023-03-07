from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import JSONResponse
from typing import List

from app.db import DatabaseManager
from app.utils.constants import get_responses, put_responses, patch_responses, get_list_responses
from app.db import get_db
from app.db.models import Lesson


router = APIRouter(
    prefix='/lessons',
    tags=['lessons']
)


@router.get('/', tags=['lessons'], responses=get_list_responses(model=Lesson))
async def get_all_lessons(db: DatabaseManager = Depends(get_db)) -> List[Lesson]:
    rooms = await db.get_lessons_all()
    return rooms


@router.get('/{lesson_id}', tags=['lessons'], responses=get_responses(model=Lesson))
async def get_lesson(lesson_id: str, db: DatabaseManager = Depends(get_db)):
    lesson = await db.get_lesson(lesson_id=lesson_id)
    if not lesson:
        raise HTTPException(status_code=404, detail=f'Room {id} not found')
    return lesson


@router.put('/', response_description="Add new room", responses=put_responses(model=Lesson))
async def create_lesson(payload: Lesson, db: DatabaseManager = Depends(get_db)):
    lesson_created = await db.lesson_insert_one(lesson=payload)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=lesson_created)


@router.patch('/', response_description="", responses=patch_responses(model=Lesson))
async def patch_lesson(payload: Lesson, db: DatabaseManager = Depends(get_db)):
    lesson_updated = await db.patch_lesson(lesson=payload)
    return lesson_updated
