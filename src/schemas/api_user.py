from datetime import datetime
from src.schemas.base_schema import BaseSchema as BaseModel

class ApiUser(BaseModel):
    username: str
    password: str

class ApiUserUpdate(BaseModel):
    username: str = None
    password: str = None
    responsible_cpf: str = None
    responsible_email: str = None
    is_active: bool = None

class ApiUserResponse(BaseModel):
    username: str = None
    responsible_cpf: str = None
    responsible_email: str = None
    is_a_robot: bool = None
    is_active: bool = None

class TokenResponse(BaseModel):
    username: str
    token: str
    expiration_time: int