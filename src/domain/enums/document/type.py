from enum import Enum

class DocumentType(str, Enum):
    README = "README"
    METHODOLOGY = "Methodology"
    RESEARCH_NOTE = "Research Note"
    REPORT = "Report"
    ADR = "ADR"
    OTHER = "Other"