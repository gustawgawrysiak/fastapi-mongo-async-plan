from bson import ObjectId
from typing import Dict, Any, List, Type
from pydantic import BaseModel

from starlette import status


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Error(BaseModel):
    detail: int
    status_code: str

    class Config:
        schema_extra = {
            "example": {
                "detail": "Not found",
                "status_code": 404
            }
        }


def get_responses(model: Type) -> Dict[int, dict]:
    return {
        status.HTTP_404_NOT_FOUND: {"model": Error},
        status.HTTP_200_OK: {"model": model}
    }


def get_list_responses(model: Type) -> Dict[int, dict]:
    return {
        status.HTTP_404_NOT_FOUND: {"model": Error},
        status.HTTP_200_OK: {"model": List[model]}
    }


def patch_responses(model: Type) -> Dict[int, dict]:
    return {
        status.HTTP_409_CONFLICT: {"model": Error},
        status.HTTP_202_ACCEPTED: {"model": model},
    }


def put_responses(model: Type) -> Dict[int, dict]:
    return {
        status.HTTP_409_CONFLICT: {"model": Error},
        status.HTTP_201_CREATED: {"model": model}
    }
