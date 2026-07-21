from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

class Metadata(BaseModel):
    model_config = {"from_attributes": True}
    
    total: int
    limit: int
    offset: int

class PaginatedResponse(BaseModel, Generic[T]):
    model_config = {"from_attributes": True}

    data: list[T]
    meta: Metadata