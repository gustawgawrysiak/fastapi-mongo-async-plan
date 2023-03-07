from pydantic import BaseModel, Field
from bson import ObjectId
from app.utils.constants import PyObjectId
from typing import Optional


class Room(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str = Field(...)
    description: str = Field(...)
    category: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "123A",
                "description": "Mathematics lesson",
                "category": "classroom"
            }
        }


class UpdateRoom(BaseModel):
    name: Optional[str]
    description: Optional[str]
    category: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "123A",
                "description": "Mathematics lesson",
                "category": "classroom"
            }
        }
