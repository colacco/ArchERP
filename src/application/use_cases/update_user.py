from datetime import datetime
from uuid import UUID


from src.domain.entities.user import User
from src.domain.value_objects.email import Email
from src.domain.repositories.role_reader import RoleReader
from src.domain.repositories.user_repository import UserRepository
from src.domain.exceptions.user_not_found import UserNotFound
from src.domain.exceptions.email_already_in_use import EmailAlreadyInUse
from src.domain.exceptions.role_not_found import RoleNotFound


from src.application.dtos.update_user_input import UpdateUserInput
from src.application.dtos.user_output import UserOutput

class UpdateUser():
    def __init__(self, repository: UserRepository, role_repository: RoleReader):
        self._repository = repository
        self._role = role_repository
    
    def _ensure_email_is_available(self, new_Email: str, current_user_id: UUID) -> None:
        owner: User | None = self._repository.get_user_by_email(new_Email)

        if owner is not None and owner.id != current_user_id:
            raise EmailAlreadyInUse(new_Email)

    def _ensure_role_exist(self, role_id: UUID) -> None:
        role = self._role.get_role_by_id(role_id)

        if role is None:
            raise RoleNotFound(role_id)

    def execute(self, id: UUID, dto: UpdateUserInput) -> UserOutput:
        user = self._repository.get_user_by_id(id)

        if user is None: 
            raise UserNotFound(id)
        if dto.role_id is not None:
            self._ensure_role_exist(dto.role_id)
        if dto.email is not None:
            self._ensure_email_is_available(dto.email, user.id)
        
        if dto.name is not None:
            user.name = dto.name
        if dto.email is not None:
            user.email = Email(dto.email)
        if dto.role_id is not None:
            user.role_id = dto.role_id
        user.updated_at = datetime.now()

        user = self._repository.update_user(user, id)
        return UserOutput.from_entity(user)
