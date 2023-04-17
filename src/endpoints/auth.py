from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException

from src.dependencies import database
from src.schemas.api_user import ApiUser, TokenResponse
from src.services.auth_service import AuthService

router = APIRouter(
    prefix = '/auth',
    tags = ['Authorization', 'Login']
)

@router.post("", response_model = TokenResponse, status_code = status.HTTP_200_OK)
async def get_all(auth: ApiUser, db: Session = Depends(database.get_db)):
    auth = AuthService.auth(auth, db)

    if auth:
        return auth
    raise HTTPException(status_code = 403, detail = "Access denied")