from typing import Annotated, Any, Callable

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from  fastapi import Depends, HTTPException

from src.application.ports.token_service import TokenService

from src.presentation.http.dependencies import get_token_service

def get_current_user( 
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())], 
    token_service: Annotated[TokenService, Depends(get_token_service)]
) -> dict[str, Any]:
    payload = token_service.verify(credentials.credentials)
    
    if payload is None:
        raise HTTPException(401, "Invalid or expired token")
    
    return payload

def require_role(role: str) -> Callable[ [dict[str, Any]], dict[str, Any] ]:
    def check(current_user: Annotated[dict[str, Any], Depends(get_current_user)]) -> dict[str, Any]:
        if current_user["role"] != role:
            raise HTTPException(status_code=403, detail="Forbidden")
        
        return current_user
    
    return check