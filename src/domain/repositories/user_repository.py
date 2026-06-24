from abc import ABC, abstractmethod

from src.domain.entities.user import User

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass

    @abstractmethod
    def get_users(self) -> list[User]:
        pass

    @abstractmethod
    def get_user_by_id(self, id: str) -> User:
        pass
    
    @abstractmethod
    def update_user(self, user: User, id: str) -> User:
        pass

    @abstractmethod
    def delete_user(self, id: str) -> User:
        pass