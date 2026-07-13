from pathlib import Path
import yt_dlp

from app.config.yt_dlp_options import DOWNLOAD_OPTIONS

class DownloadService:

    DOWNLOAD_FOLDER = Path("app/downloads")

    def download(self, url: str, format_id: str) -> Path:

        self.DOWNLOAD_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        options = DOWNLOAD_OPTIONS.copy()

        options["format"] = format_id
        options["outtmpl"] = str(
            self.DOWNLOAD_FOLDER / "%(title)s.%(ext)s"
        )

        with yt_dlp.YoutubeDL(options) as ydl:
            
            info = ydl.extract_info(
                url,
                download=True
            )

            downloaded_file = Path(
                ydl.prepare_filename(info)
            )

        return downloaded_file