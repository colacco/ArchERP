from uuid import UUID

from src.domain.repositories.role_repository import RoleRepository
from src.domain.exceptions.role_not_found import RoleNotFound

from src.application.dtos.role_output import RoleOutput

class GetRole():
    def __init__(self, repository: RoleRepository) -> None:
        self._repository = repository

    def execute(self, id: UUID) -> RoleOutput:
        role = self._repository.get_role_by_id(id)

        if role is None:
            raise RoleNotFound(id)
        
        return RoleOutput.from_entity(role)