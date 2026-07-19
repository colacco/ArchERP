import os
from dotenv import load_dotenv

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)

    if value is None:
        raise RuntimeError(f"Environment variable {name} is not defined")
    
    return value

def get_env(name: str, default: str) -> str:
    value = os.getenv(name)

    if value is None:
        return default
    
    return value