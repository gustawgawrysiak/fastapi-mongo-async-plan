from abc import abstractmethod
from typing import List

from app.db.models import Room, Lesson


class DatabaseManager:
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass

    @abstractmethod
    async def get_room(self, name: str):
        pass

    @abstractmethod
    async def get_rooms_all(self):
        pass

    @abstractmethod
    async def room_insert_one(self, room: Room) -> List[Room]:
        pass

    @abstractmethod
    async def patch_room(self, room: Room):
        pass

    @abstractmethod
    async def get_lesson(self, lesson_id: str):
        pass

    @abstractmethod
    async def get_lessons_all(self):
        pass

    @abstractmethod
    async def lesson_insert_one(self, lesson: Lesson) -> Lesson:
        pass

    @abstractmethod
    async def get_course(self, course_name):
        pass

    @abstractmethod
    async def get_course_details(self, course_name):
        pass

    @abstractmethod
    async def create_course(self, course):
        pass

    @abstractmethod
    async def get_courses_all(self):
        pass

    @abstractmethod
    async def course_insert_one(self, course):
        pass

    @abstractmethod
    async def patch_course(self, course):
        pass

    @abstractmethod
    async def patch_lesson(self, lesson):
        pass
