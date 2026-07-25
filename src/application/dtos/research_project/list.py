from dataclasses import dataclass
from datetime import datetime

@dataclass
class ListResearchProjectsInput():
    limit: int | None = None
    offset: int | None = None
    status: str | None = None
    visibility: str | None = None
    start_date: datetime | None = None
    end_date: datetime | None = None