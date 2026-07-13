from typing import Protocol
from uuid import UUID

from src.domain.entities.role import Role

class RoleReader(Protocol):
    def get_role_by_id(self, id: UUID) -> Role | None:
        pass