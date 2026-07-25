from uuid import UUID

class RoleNotFound(Exception):
    def __init__(self, role_id: UUID):
        super().__init__(f"Role {role_id} not found")