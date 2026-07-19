from copy import deepcopy
from uuid import UUID

from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.user_not_found import UserNotFound

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users: list[User] = []

    def create_user(self, user: User) -> User:
        self.users.append(deepcopy(user))
        return user
    
    def get_users(self) -> list[User]:
        return deepcopy(self.users)

    def get_user_by_id(self, id: UUID) -> User | None:
        user = next((user for user in self.users if user.id == id), None)
        return deepcopy(user)
    
    def get_user_by_email(self, email: str) -> User | None:
        user = next((user for user in self.users if user.email.value == email), None)
        return deepcopy(user)

    def update_user(self, user: User, id: UUID) -> User:
        index = next((i for i, u in enumerate(self.users) if u.id == id), None)

        if index is None:
            raise UserNotFound(id)
        
        self.users[index] = deepcopy(user)
        
        return user

    def delete_user(self, id: UUID) -> User:
        index = next((i for i, u in enumerate(self.users) if u.id == id), None)

        if index is None:
            raise UserNotFound(id) 

        return self.users.pop(index)
    
    def has_user_with_role_id(self, role_id: UUID) -> bool:
        for user in self.users:
            if user.role_id == role_id:
                return True
            
        return False