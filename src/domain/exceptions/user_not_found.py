class UserNotFound(Exception):
    def __init__(self, user_id: str):
        super().__init__(f"User {user_id} not found")