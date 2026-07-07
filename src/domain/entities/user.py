from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from ..value_objects.email import Email

@dataclass
class User():
    id: UUID
    role_id: UUID

    name: str
    email: Email
    password_hash: str
    
    created_at: datetime
    updated_at: datetime

    def __str__(self) -> str:
        return f"Usuário: {self.name}\n Email: {self.email}"
