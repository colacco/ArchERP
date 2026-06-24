from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.application.dtos.user_output import UserOutput

class GetUser():
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def _to_output(self, user: User):
        return UserOutput(id=user.id, name=user.name, email=user.email.value, role_id=user.role_id)

    def execute(self):
        users = self._repository.get_users()
        return [self._to_output(user) for user in users]