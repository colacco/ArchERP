from src.domain.repositories.user_repository import UserRepository
from src.application.dtos.user_output import UserOutput

class GetUsers():
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self) -> list[UserOutput]:
        users = self._repository.get_users()
        return [UserOutput.from_entity(user) for user in users]