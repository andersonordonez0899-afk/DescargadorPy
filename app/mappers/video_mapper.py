from app.schemas.video import Video, VideoFormat

class VideoMapper:
    """Mapea la información obtenida por yt-dlp a modelos de dominio """
    @staticmethod
    def to_video(info: dict) -> Video:
        formats = []
        seen = set()
        
        for fmt in info.get("formats", []):

            # Ignorar si el formato es solo audio (sin pista de video)
            if fmt.get("vcodec") == "none":
                continue

            # 1. Intentar obtener la nota de formato directa 
            quality = fmt.get("format_note")
            
            # 2. Si no existe, construirla usando la altura numérica 
            if not quality and fmt.get("height"):
                quality = f"{fmt.get('height')}p"
                
            # 3. Si no hay altura, usar el ancho como alternativa 
            if not quality and fmt.get("width"):
                quality = f"{fmt.get('width')}w"
                
            # 4. Respaldo final si yt-dlp no provee ninguna dimensión
            if not quality:
                quality = "Video"

            extension = fmt.get("ext", "")

            # Clave única combinando calidad real obtenida y extensión (ej. ('240p', 'mp4'))
            key = (quality, extension)

            if key in seen:
                continue

            seen.add(key)

            formats.append(
                VideoFormat(
                    id=fmt.get("format_id", ""),
                    extension=extension,
                    quality=quality,
                    filesize=fmt.get("filesize"),
                    type="video"
                )
            )
            
        return Video(
            title=info.get("title", ""),
            uploader=info.get("uploader", ""),
            duration=int(float(info.get("duration", 0))),
            thumbnail=info.get("thumbnail", ""),
            platform=info.get("extractor", ""),
            webpage_url=info.get("webpage_url", ""),
            formats=formats,
        )
