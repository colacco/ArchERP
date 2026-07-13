from dataclasses import dataclass
from datetime import datetime
from typing import Self
from uuid import UUID

from src.domain.entities.role import Role

@dataclass
class RoleOutput():
    id: UUID
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, role: Role) -> Self:
        return cls(
            id=role.id,
            name=role.name,
            description=role.description,
            created_at=role.created_at,
            updated_at=role.updated_at
        )