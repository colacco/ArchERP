from uuid import UUID

class ResearchProjectNotFound(Exception):
    def __init__(self, research_project_id: UUID):
        super().__init__(f"Research project {research_project_id} not found")