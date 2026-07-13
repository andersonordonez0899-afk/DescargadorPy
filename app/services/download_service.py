from pathlib import Path
import yt_dlp

from app.config.yt_dlp_options import DOWNLOAD_OPTIONS

class DownloadService:

    DOWNLOAD_FOLDER = Path("app/downloads")

    def download(self, url: str, format_id: str):

        print("=" * 50)
        print("Iniciando descarga")
        print(f"URL: {url}")
        print(f"Format ID: {format_id}")
        print(f"Destino: {self.DOWNLOAD_FOLDER.resolve()}")

        self.DOWNLOAD_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        options = DOWNLOAD_OPTIONS.copy()

        options["format"] = format_id
        options["outtmpl"] = str(
            self.DOWNLOAD_FOLDER / "%(title)s.%(ext)s"
        )

        print(options)

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("Descarga termianda")
        print("=" * 50)