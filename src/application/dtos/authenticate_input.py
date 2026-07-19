from dataclasses import dataclass

@dataclass
class AuthenticateInput:
    email: str
    password: str