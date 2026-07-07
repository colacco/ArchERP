class EmailAlreadyInUse(Exception):
    def __init__(self, email: str):
        super().__init__(f"Email {email} already in use")