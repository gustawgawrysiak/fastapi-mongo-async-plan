from pydantic import BaseModel, Field
from app.utils.constants import PyObjectId
from bson import ObjectId
from typing import Optional


class Subject(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    name: str = Field(...)
    description: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Mathematics",
                "description": "Mathematics subject"
            }
        }


class UpdateSubject(BaseModel):
    name: Optional[str]
    description: Optional[str]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "name": "Mathematics",
                "description": "Mathematics subject"
            }
        }
