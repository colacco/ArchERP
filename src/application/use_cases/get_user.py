from src.domain.entities.user import User
from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.user_not_found import UserNotFound

from src.application.dtos.user_output import UserOutput

class GetUser():
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, id:str):
        user: User = self._repository.get_user_by_id(id)
        
        if not user:
            raise UserNotFound(id)
        
        return UserOutput(
            id=user.id, 
            role_id=user.role_id, 
            name=user.name, 
            email=user.email.value
        )