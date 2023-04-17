import os
import time
from typing import Dict

import jwt

JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')

def sign_jwt(username: str) -> Dict[str, str]:
    payload = {
        'username': username,
        'expires': time.time() + 300
    }
    return jwt.encode(payload, JWT_SECRET, algorithm = JWT_ALGORITHM)

def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms = [JWT_ALGORITHM])
        return decoded_token if decoded_token['expires'] >= time.time() else None
    except:
        return None