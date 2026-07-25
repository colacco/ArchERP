from uuid import UUID

class UserNotFound(Exception):
    def __init__(self, user_id: UUID):
        super().__init__(f"User {user_id} not found")