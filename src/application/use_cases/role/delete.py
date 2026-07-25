from uuid import UUID

from src.domain.repositories.role_repository import RoleRepository
from src.domain.repositories.user_role_checker import UserRoleChecker
from src.domain.exceptions.role.not_found import RoleNotFound
from src.domain.exceptions.role.being_used import RoleBeingUsed

from src.application.dtos.role.output import RoleOutput

class DeleteRole():
    def __init__(self, repository: RoleRepository, user_repository: UserRoleChecker) -> None:
        self._repository = repository
        self._user = user_repository

    def execute(self, id: UUID) -> RoleOutput:
        if self._user.has_user_with_role_id(id):
            raise RoleBeingUsed(id)
        
        role = self._repository.delete_role(id)

        if role is None:
            raise RoleNotFound(id)

        return RoleOutput.from_entity(role)