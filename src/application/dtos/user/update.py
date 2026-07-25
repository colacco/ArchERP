from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class UpdateUserInput():
    name: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[UUID] = None
