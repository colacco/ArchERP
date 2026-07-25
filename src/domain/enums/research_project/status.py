from enum import Enum

class ResearchProjectStatus(str, Enum):
    PAUSED = "paused"
    PLANNING = "planning"
    RUNNING = "running"
    FINISHED = "finished"
    ARCHIVED = "archived"