from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_users(self) -> list[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, id: UUID) -> User | None:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User | None:
        pass
    
    @abstractmethod
    def update_user(self, user: User, id: UUID) -> User:
        pass

    @abstractmethod
    def delete_user(self, id: UUID) -> User:
        pass

    @abstractmethod
    def has_user_with_role_id(self, role_id: UUID) -> bool:
        pass