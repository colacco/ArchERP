from src.application.use_cases.createUser import CreateUser
from src.application.dtos.create_user_input import CreateUserInput
from src.domain.repositories.user_repository import UserRepository
from src.domain.entities.user import User

class InMemoryUserRepository(UserRepository):
    def create_user(self, user: User) -> User:
        return user
    
    def get_user(self) -> User:
        pass

    def get_user_by_id(self, id: str) -> User:
        pass
    
    def update_user(self, user: User) -> User:
        pass

    def delete_user(self, id: str) -> User:
        pass

use_case = CreateUser(InMemoryUserRepository())
print(use_case.execute(CreateUserInput("Gabriel", "email@email.com", "1234")))