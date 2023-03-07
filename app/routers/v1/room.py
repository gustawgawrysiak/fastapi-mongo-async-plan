from fastapi import APIRouter, Depends, HTTPException, status
from starlette.responses import JSONResponse
from typing import List

from app.db import DatabaseManager
from app.utils.constants import get_responses, put_responses, patch_responses, get_list_responses
from app.db import get_db
from app.db.models import Room


router = APIRouter(
    prefix='/rooms',
    tags=['rooms']
)


@router.get('/', tags=['rooms'], responses=get_list_responses(model=Room))
async def get_all_rooms(
        db: DatabaseManager = Depends(get_db)
) -> List[Room]:
    rooms = await db.get_rooms_all()
    return rooms


@router.get('/room/{room_name}', tags=['rooms'], responses=get_responses(model=Room))
async def get_room(room_name: str, db: DatabaseManager = Depends(get_db)):
    room = await db.get_room(name=room_name)
    if not room:
        raise HTTPException(status_code=404, detail=f'Room {id} not found')
    return room


@router.put('/room/', response_description="Add new room", responses=put_responses(model=Room))
async def create_room(payload: Room, db: DatabaseManager = Depends(get_db)):
    room_created = await db.room_insert_one(room=payload)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=room_created)


@router.patch('/room/', response_description="", responses=patch_responses(model=Room))
async def patch_room(payload: Room, db: DatabaseManager = Depends(get_db)):
    room_updated = await db.patch_room(room=payload)
    return room_updated
