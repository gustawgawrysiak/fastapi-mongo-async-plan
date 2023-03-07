import os
import logging
from fastapi import FastAPI
from app.routers.api import api_router
from app.db import db


""" FastAPI async API for lesson plan using Mongo"""


"""
    TODO:
        1. Lessons for each course grouped by days
        2. Routes for lecturer, lesson
        3. Settings from class obj
        4. Custom logging for specific ENV
        5. Basic front plan display
        6. Admin
"""


log = logging.getLogger(__name__)


server = FastAPI(
    docs_url='/'
)


server.include_router(api_router)


log.info(
    f"Lesson plan API has been launched"
)


@server.on_event("startup")
async def startup_db_client():
    log.info("Database connection startup")
    await db.connect_to_database(os.environ["MONGODB_URL"])


@server.on_event("shutdown")
async def shutdown_db_client():
    log.info("Database connection shutdown")
    await db.close_database_connection()
