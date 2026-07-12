from app.schemas.video import Video
from app.config.yt_dlp_options import YDL_OPTIONS
from app.mappers.video_mapper import VideoMapper
import yt_dlp



class VideoService:
    """obtiene la info del video con yt-dlp"""
    def get_information(self, url: str) -> Video:
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            information = ydl.extract_info(
                url, 
                download=False
                )
        return VideoMapper.to_video(information)
    