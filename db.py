import encodings
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


mysql_db_name = os.getenv('MYSQL_DBNAME')
mysql_db_username = os.getenv('MYSQL_USER')
mysql_db_user_password = os.getenv('MYSQL_PASSWORD')
mysql_service_host = os.getenv('MYSQL_SERVICE_HOST')
mysql_service_port = int(os.getenv('MYSQL_SERVICE_PORT', 3306))

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{mysql_db_username}:{mysql_db_user_password}@{mysql_service_host}:{mysql_service_port}/{mysql_db_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('DB_TRACK_MODIFICATIONS', False)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    encoding="utf-8",
    echo=True
)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = declarative_base()