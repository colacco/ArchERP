from uuid import UUID
from datetime import datetime

from src.domain.repositories.role_repository import RoleRepository
from src.domain.exceptions.role_not_found import RoleNotFound

from src.application.dtos.update_role_input import UpdateRoleInput
from src.application.dtos.role_output import RoleOutput

class UpdateRole():
    def __init__(self, repository: RoleRepository) -> None:
        self._repository = repository

    def execute(self, dto: UpdateRoleInput, id: UUID) -> RoleOutput:
        role = self._repository.get_role_by_id(id)

        if role is None:
            raise RoleNotFound(id)
        
        if dto.name is not None:
            role.name = dto.name

        if dto.description is not None:
            role.description = dto.description

        role.updated_at = datetime.now()

        role = self._repository.update_role(role, id)

        return RoleOutput.from_entity(role)