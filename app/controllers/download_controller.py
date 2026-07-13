from fastapi import APIRouter, Form
from fastapi.responses import FileResponse

from app.schemas.url_request import UrlRequest

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
def download_video(
    url: str = Form(...),
    format_id: str = Form(...)
):

    file_path = download_service.download(
        url,
        format_id
    )

    return FileResponse(
        path=file_path,
        filename=file_path.name,
        media_type="application/octet-stream"
    )