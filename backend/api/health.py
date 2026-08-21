from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def health_check():

    return {
        "success": True,
        "status": "ok",
        "service": "mindbridge-api",
        "version": "1.0.0",
    }