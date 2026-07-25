from uuid import UUID

from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.user.not_found import UserNotFound

from src.application.dtos.user.output import UserOutput

class GetUser():
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, id: UUID) -> UserOutput:
        user = self._repository.get_user_by_id(id)
        
        if user is None:
            raise UserNotFound(id)
        
        return UserOutput.from_entity(user)