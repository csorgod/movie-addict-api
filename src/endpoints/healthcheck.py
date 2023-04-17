from fastapi import APIRouter

router = APIRouter(
    tags=["Healthcheck"],
    responses={ 404: { "description": "Not found" } },
)

@router.get("/")
async def healthcheck():
    return "Alive!"