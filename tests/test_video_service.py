from app.services.video_service import VideoService

service = VideoService()

video = service.get_information(
    "https://www.youtube.com/watch?v=jNQXAC9IVRw"
    )
print(video.title)
print(video.uploader)
print(video.duration)