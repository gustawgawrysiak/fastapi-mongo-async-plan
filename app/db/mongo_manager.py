import json
import logging
from fastapi import HTTPException
from starlette import status
from typing import List, Dict
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from bson.json_util import dumps
from .db_manager import DatabaseManager
from .models import Room, Lesson

log = logging.getLogger(__name__)


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, path: str):
        log.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(
            path,
            maxPoolSize=10,
            minPoolSize=10)
        self.db = self.client.plan
        log.info("Connected to MongoDB.")

    async def close_database_connection(self):
        log.info("Closing connection with MongoDB.")
        self.client.close()
        log.info("Closed connection with MongoDB.")

    async def get_room(self, name: str) -> Room:
        rooms = self.db.rooms.find({"name": name})
        if not rooms:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Room {name} not found"
            )
        async for room in rooms:
            del room["_id"]
            return json.loads(dumps(room))

    async def get_rooms_all(self) -> List[Dict[str, str]]:
        response_list: List[dict] = []
        rooms = self.db.rooms.find()
        async for room in rooms:
            response_list.append(room)
        return response_list

    async def room_insert_one(self, room: Room) -> Room:
        room_dict = room.dict()
        name = room_dict["name"]
        room_exist: bool = await self.db.rooms.count_documents({"name": name}) > 0
        if room_exist:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Room {name} already exist"
            )

        await self.db.rooms.insert_one(room_dict)
        response = await self.get_room(name)
        return response

    async def patch_room(self, room: Room):
        _room = room.dict()
        await self.db.rooms.update_one({"name": _room["name"]}, {"$set": _room})
        room_updated = await self.get_room(name=_room["name"])
        return room_updated

    async def get_lesson(self, lesson_id: str):
        lessons = self.db.lessons.find({"_id": lesson_id})
        if not lessons:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Lesson {lesson_id} not found"
            )
        async for lesson in lessons:
            return json.loads(dumps(lesson))

    async def get_lessons_all(self):
        response_list: List[dict] = []
        lessons = self.db.lessons.find()
        async for lesson in lessons:
            response_list.append(lesson)
        return response_list

    async def lesson_insert_one(self, lesson: Lesson) -> Lesson:
        lesson_dict = lesson.dict()
        _id = lesson_dict["_id"]
        room_exist: bool = await self.db.rooms.count_documents({"_id": _id}) > 0
        if room_exist:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Lesson {_id} already exist"
            )
        await self.db.lessons.insert_one(lesson_dict)
        response = await self.get_lesson(_id)
        return response

    async def patch_lesson(self, lesson: Lesson):
        _lesson = lesson.dict()
        await self.db.rooms.update_one({"_id": _lesson["_id"]}, {"$set": _lesson})
        room_updated = await self.get_lesson(lesson_id=_lesson["_id"])
        return room_updated

    async def get_course_details(self, course_name):
        return
