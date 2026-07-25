from uuid import uuid4
from datetime import datetime

from src.domain.entities.role import Role
from src.domain.repositories.role_repository import RoleRepository

from src.application.dtos.role.create import CreateRoleInput
from src.application.dtos.role.output import RoleOutput

class CreateRole():
    def __init__(self, repository: RoleRepository) -> None:
        self._repository = repository

    def execute(self, dto: CreateRoleInput) -> RoleOutput:
        role = Role(
            id=uuid4(),
            name=dto.name,
            description=dto.description,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        role = self._repository.create_role(role)
        
        return RoleOutput.from_entity(role)