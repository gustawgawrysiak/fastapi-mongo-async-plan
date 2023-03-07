from pydantic import BaseModel, Field
from app.utils.constants import PyObjectId
from bson import ObjectId
from typing import Optional


class Lesson(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    course_id: int = Field(...)
    weekday: int = Field(..., ge=1, le=7)
    hour_start: str = Field(..., max_length=5)
    hour_end: str = Field(..., max_length=5)
    subject_id: int = Field(...)
    description: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "course_id": "1",
                "weekday": "1",
                "hour_start": "10:00",
                "hour_end": "11:30",
                "subject_id": "1",
                "description": "PE lesson"
            }
        }


class UpdateLesson(BaseModel):
    course_id: Optional[int]
    weekday: Optional[int]
    hour_start: Optional[int]
    hour_end: Optional[int]
    subject_id: Optional[int]
    description: Optional[int]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "course_id": "1",
                "weekday": "1",
                "hour_start": "10:00",
                "hour_end": "11:30",
                "subject_id": "1",
                "description": "PE lesson"
            }
        }