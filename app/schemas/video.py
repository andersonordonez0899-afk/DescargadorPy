from pydantic import BaseModel

class VideoFormat(BaseModel):
    id: str
    extension: str
    quality: str
    filesize: int | None = None
    type: str

class Video(BaseModel):
    title: str
    uploader: str
    duration: int
    thumbnail: str
    platform: str
    webpage_url: str
    formats: list[VideoFormat]
    