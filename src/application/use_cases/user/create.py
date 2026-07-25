from uuid import uuid4
from datetime import datetime

from src.domain.entities.user import User
from src.domain.value_objects.email import Email
from src.domain.repositories.user_repository import UserRepository
from src.domain.repositories.role_reader import RoleReader
from src.domain.exceptions.user.email_already_in_use import EmailAlreadyInUse
from src.domain.exceptions.role.not_found import RoleNotFound

from src.application.ports.password_hasher import PasswordHasher
from src.application.dtos.user.create import CreateUserInput
from src.application.dtos.user.output import UserOutput

class CreateUser():
    def __init__(self, repository: UserRepository, role_repository: RoleReader, password_hasher: PasswordHasher):
        self._repository = repository
        self._role = role_repository
        self._hasher = password_hasher

    def execute(self, dto: CreateUserInput) -> UserOutput:
        existing_user = self._repository.get_user_by_email(dto.email)
        existing_role = self._role.get_role_by_id(dto.role_id)

        if existing_user is not None:
            raise EmailAlreadyInUse(dto.email)
        
        if existing_role is None:
            raise RoleNotFound(dto.role_id)
        
        user: User = User(
            id= uuid4(),
            role_id= dto.role_id,
            name= dto.name,
            email= Email(dto.email),
            password_hash= self._hasher.hash(dto.password),
            created_at= datetime.now(),
            updated_at= datetime.now()
        )

        user = self._repository.create_user(user)
        
        return UserOutput.from_entity(user)