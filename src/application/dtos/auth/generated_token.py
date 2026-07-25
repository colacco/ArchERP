from dataclasses import dataclass

@dataclass
class GeneratedToken:
    token: str
    expires_in: int 