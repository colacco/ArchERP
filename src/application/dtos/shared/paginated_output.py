from dataclasses import dataclass
from typing import TypeVar, Generic

T = TypeVar("T")

@dataclass
class PaginatedOutput(Generic[T]):
    items: list[T]
    total: int
    limit: int
    offset: int