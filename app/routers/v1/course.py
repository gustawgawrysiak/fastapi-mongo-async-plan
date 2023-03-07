from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import JSONResponse
from typing import List

from app.db import DatabaseManager
from app.utils.constants import get_responses, put_responses, patch_responses, get_list_responses
from app.db import get_db
from app.db.models import Course


router = APIRouter(
    prefix='/course',
    tags=['courses']
)


@router.get('/', responses=get_list_responses(model=Course))
async def get_all_courses(db: DatabaseManager = Depends(get_db)) -> List[Course]:
    courses = await db.get_courses_all()
    return courses


@router.get('/course/{course_id}', responses=get_responses(model=Course))
async def get_course(course_name: str, db: DatabaseManager = Depends(get_db)):
    course = await db.get_course(course_name=course_name)
    if not course:
        raise HTTPException(status_code=404, detail=f'Course {id} not found')
    return course


@router.get('/course/details/{course_id}', responses=get_responses(model=Course))
async def get_course_details(course_name: str, db: DatabaseManager = Depends(get_db)):
    course = await db.get_course_details(course_name=course_name)
    if not course:
        raise HTTPException(status_code=404, detail=f'Course {course_name} not found')
    return course


@router.put('/room/', response_description="Add new course", responses=put_responses(model=Course))
async def create_course(payload: Course, db: DatabaseManager = Depends(get_db)):
    course_created = await db.course_insert_one(course=payload)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=course_created)


@router.patch('/room/', response_description="", responses=patch_responses(model=Course))
async def patch_course(payload: Course, db: DatabaseManager = Depends(get_db)):
    course_updated = await db.patch_course(course=payload)
    return course_updated
