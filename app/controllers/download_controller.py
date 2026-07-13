from fastapi import APIRouter

from app.schemas.url_request import UrlRequest
from app.schemas.download_request import DownloadRequest

from app.services.video_service import VideoService
from app.services.download_service import DownloadService


router = APIRouter(
    prefix="/download",
    tags=["download"]
)

video_service = VideoService()
download_service = DownloadService()

@router.post("/info")
def get_video_information(data: UrlRequest):
    return video_service.get_information(data.url)

@router.post("/")
def download_video(data: DownloadRequest):
    download_service.download(
        data.url,
        data.format_id
        ) 
    return{
        "message": "Descarga completada"
    }