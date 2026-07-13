from dataclasses import dataclass

@dataclass
class CreateRoleInput():
    name: str
    description: str