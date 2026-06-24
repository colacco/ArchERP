from datetime import datetime

from src.domain.value_objects.email import Email
from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.user_not_found import UserNotFound
from src.application.dtos.update_user_input import UpdateUserInput
from src.application.dtos.user_output import UserOutput

class UpdateUser():
    def __init__(self, repository: UserRepository):
        self._repository = repository
    
    def execute(self, id: str, dto: UpdateUserInput):
        user = self._repository.get_user_by_id(id)

        if not user: raise UserNotFound(id)
        
        if dto.name is not None:
            user.name = dto.name
        if dto.email is not None:
            user.email = Email(dto.email)
        user.updated_at = datetime.now()

        user = self._repository.update_user(user, id)
        return UserOutput(user.id, user.role_id, user.name, user.email.value)
