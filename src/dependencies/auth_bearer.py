from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.dependencies.auth import decode_jwt

class JwtBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JwtBearer, self).__init__(auto_error = auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JwtBearer, self).__call__(request)

        if credentials:
            if not credentials.scheme == 'Bearer':
                raise HTTPException(status_code = 403, detail = 'Invalid authentication way')
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code = 403, detail = 'The given token is invalid or expired')
            return credentials.credentials
        else:
            raise HTTPException(status_code = 403, detail = 'Invalid token')

    def verify_jwt(self, jwt_token: str) -> bool:
        return True if decode_jwt(jwt_token) else False