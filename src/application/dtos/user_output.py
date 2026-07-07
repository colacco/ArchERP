from uuid import UUID
from typing import Self
from dataclasses import dataclass

from src.domain.entities.user import User

@dataclass
class UserOutput():
    id: UUID
    role_id: UUID
    name: str
    email: str

    @classmethod
    def from_entity(cls, user: User) -> Self:
        return cls(
            id= user.id,
            role_id= user.role_id,
            name= user.name,
            email= user.email.value
        )