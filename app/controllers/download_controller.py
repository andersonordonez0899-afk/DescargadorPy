from fastapi import APIRouter

router = APIRouter(
    prefix="/download",
    tags=["download"]
)

@router.post("/info")
def get_video_information():
    return{
        "status": "ok"
    }