from app.schemas.video import Video, VideoFormat

class VideoMapper:
    """Mapea la información obtenida por yt-dlp a modelos de dominio """
    @staticmethod
    def to_video(info: dict) -> Video:
        formats = []
        for fmt in info.get("formats", []):
            if fmt.get("vcodec") == "none":
                continue
            formats.append(
                VideoFormat(
                    id=fmt.get("format_id", ""),
                    extension=fmt.get("ext", ""),
                    quality=fmt.get("format_note", "Desconocida"),
                    filesize=fmt.get("filesize"),
                    type="video"
                )
            )
        return Video(
            title=info.get("title", ""),
            uploader=info.get("uploader", ""),
            duration=info.get("duration", 0),
            thumbnail=info.get("thumbnail", ""),
            platform=info.get("extractor", ""),
            webpage_url=info.get("webpage_url", ""),
            formats=formats
        )