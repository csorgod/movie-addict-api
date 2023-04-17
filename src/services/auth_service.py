import logging
from datetime import datetime

import bcrypt
from sqlalchemy import desc
from sqlalchemy.orm import Session
from src.dependencies.auth import sight_jwt

from src.models.api_user import APIUser as AuthModel
from src.schemas.api_user import ApiUser, TokenResponse

class AuthService():

    def auth(auth: ApiUser, db: Session):

        user = db.query(AuthModel).filter(AuthModel.username == auth.username).first()

        if user:
            if bcrypt.checkpw((auth.password).encode('utf-8'), (str(user.password)).encode()):
                token = sight_jwt(auth.username)

                return TokenResponse(
                    username = auth.username,
                    token = token,
                    generated_at = datetime.now(),
                    expiration_time = 300
                )

        return None