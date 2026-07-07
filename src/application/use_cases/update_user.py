from datetime import datetime
from uuid import UUID

from src.domain.entities.user import User
from src.domain.value_objects.email import Email
from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.user_not_found import UserNotFound
from src.domain.exceptions.email_already_in_use import EmailAlreadyInUse


from src.application.dtos.update_user_input import UpdateUserInput
from src.application.dtos.user_output import UserOutput

class UpdateUser():
    def __init__(self, repository: UserRepository):
        self._repository = repository
    
    def _ensure_email_is_available(self, new_Email: str, current_user_id: UUID) -> None:
        owner: User | None = self._repository.get_user_by_email(new_Email)

        if owner is not None and owner.id != current_user_id:
            raise EmailAlreadyInUse(new_Email)

    def execute(self, id: UUID, dto: UpdateUserInput) -> UserOutput:
        user: User | None = self._repository.get_user_by_id(id)

        if user is None: 
            raise UserNotFound(id)
        
        if dto.email is not None:
            self._ensure_email_is_available(dto.email, user.id)
        
        if dto.name is not None:
            user.name = dto.name
        if dto.email is not None:
            user.email = Email(dto.email)
        user.updated_at = datetime.now()

        user = self._repository.update_user(user, id)
        return UserOutput.from_entity(user)
