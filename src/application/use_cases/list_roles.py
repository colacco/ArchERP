from src.application.dtos.role_output import RoleOutput
from src.domain.repositories.role_repository import RoleRepository

class ListRoles():
    def __init__(self, repository: RoleRepository) -> None:
        self._repository = repository

    def execute(self) -> list[RoleOutput]:
        roles = self._repository.list_roles()
        return [RoleOutput.from_entity(role) for role in roles]