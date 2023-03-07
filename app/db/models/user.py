from pydantic import BaseModel, Field, EmailStr
from app.utils.constants import PyObjectId
from bson import ObjectId


class User(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "john@doe.com",
            }
        }
