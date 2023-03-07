from pydantic import BaseModel, Field
from app.utils.constants import PyObjectId
from bson import ObjectId
from typing import Optional


class Lecturer(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str = Field(...)
    surname: str = Field(...)
    description: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "John",
                "surname": "Doe",
                "description": "PE teacher"
            }
        }


class UpdateLecturer(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    description: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "John",
                "surname": "Doe",
                "description": "PE teacher"
            }
        }
