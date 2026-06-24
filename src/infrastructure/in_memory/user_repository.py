from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: list[User] = []

    def create_user(self, user: User) -> User:
        
        for u in self.users:
            if u.id == user.id:
                raise ConnectionRefusedError("id já existente")

        self.users.append(user)
        return user
    
    def get_users(self) -> list[User]:
        return self.users

    def get_user_by_id(self, id: str) -> User:
        return next((user for user in self.users if user.id == id), None)
    
    def update_user(self, data: User, id: str) -> User:
        user = self.get_user_by_id(id)

        if not user:
            return None
        
        for key, value in vars(data).items():
            if value is not None:
                setattr(user, key, value)
        
        return user

    def delete_user(self, id: str) -> User:
        user = self.get_user_by_id(id)

        if not user:
            return None
        
        self.users.remove(user)
        return user