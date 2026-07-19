from uuid import UUID
from typing import Protocol

class UserRoleChecker(Protocol):
    def has_user_with_role_id(self, role_id: UUID) -> bool:
        raise NotImplementedError()