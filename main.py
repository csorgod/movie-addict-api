import logging

import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from db import db, engine
from config import settings
from src.dependencies import database
from config.logging import log_config
from src.routes.api import router as api_router
from src.middlewares.logger import RequestLogger, ExceptionLogger


logging.config.dictConfig(log_config)

def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        debug=settings.DEBUG,
        log_level=settings.LOG_LEVEL,
        host=settings.HOST,
        port=settings.PORT,
        dependencies=[
            Depends(database.get_db)
        ]
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS
    )
    app.add_middleware(RequestLogger)
    app.add_middleware(ExceptionLogger)

    app.include_router(api_router)

    return app

app = get_application()
db.metadata.create_all(bind = engine)

if __name__ == '__main__':
    uvicorn.run(app = settings.APP, 
                host = settings.HOST,
                port = settings.PORT, 
                log_level = settings.LOG_LEVEL, 
                reload = settings.RELOAD
    )
    logging.info("Application is running.. Press Ctrl + C to shutdown.")
