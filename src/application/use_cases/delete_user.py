from uuid import UUID

from src.domain.exceptions.user_not_found import UserNotFound
from src.domain.repositories.user_repository import UserRepository
from src.application.dtos.user_output import UserOutput

class DeleteUser():
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, id: UUID) -> UserOutput:
        user = self._repository.get_user_by_id(id)

        if user is None:
            raise UserNotFound(id)
        
        user = self._repository.delete_user(id)

        return UserOutput.from_entity(user)