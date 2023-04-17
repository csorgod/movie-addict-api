from fastapi import APIRouter
from src.endpoints import healthcheck, movie

router = APIRouter()
router.include_router(healthcheck.router)
router.include_router(movie.router)
