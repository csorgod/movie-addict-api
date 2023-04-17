import os

PROJECT_NAME = 'Movie Addict api'
VERSION = '1.0.0'
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
LOG_LEVEL = 'debug'
HOST = '0.0.0.0'
PORT = 8086
APP = "main:app"
RELOAD = True

ALLOWED_ORIGINS = [ "http://localhost:8086" ]
IS_ALLOWED_CREDENTIALS = True
ALLOWED_METHODS = ["*"]
ALLOWED_HEADERS = ["*"]

