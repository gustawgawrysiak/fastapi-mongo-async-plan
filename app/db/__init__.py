from app.db.mongo_manager import MongoManager
from .db_manager import DatabaseManager

db = MongoManager()


async def get_db() -> DatabaseManager:
    return db
