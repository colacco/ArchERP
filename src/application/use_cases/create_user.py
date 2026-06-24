from uuid import uuid4
from datetime import datetime

from src.domain.entities.user import User
from src.domain.value_objects.email import Email
from src.domain.repositories.user_repository import UserRepository
from src.application.dtos.create_user_input import CreateUserInput
from src.application.dtos.user_output import UserOutput

class CreateUser():
    def __init__(self, repository: UserRepository):
        self._repository = repository

    def execute(self, dto: CreateUserInput):
        
        user = User(
            id= uuid4(),
            role_id= uuid4(),
            name= dto.name,
            email= Email(dto.email),
            password_hash= "",
            created_at= datetime.now(),
            updated_at= datetime.now()
        )

        user = self._repository.create_user(user)

        output = UserOutput(
            user.id, 
            user.role_id, 
            user.name, 
            user.email.value
        )
        
        return output