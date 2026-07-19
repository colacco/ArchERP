from typing import Protocol

from src.domain.entities.user import User

class UserReader(Protocol):
    def get_user_by_email(self, email: str) -> User | None:
        pass
