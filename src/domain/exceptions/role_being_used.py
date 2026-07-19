from uuid import UUID

class RoleBeingUsed(Exception):
    def __init__(self, role_id: UUID):
        super().__init__(f"Role {role_id} being used by users")