from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import yt_dlp

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; specify your frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

# Request body model
class VideoRequest(BaseModel):
    url: str

# Endpoint to download a YouTube video
@app.post("/download")
async def download_video(request: VideoRequest):
    video_url = request.url
    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    return {"message": "Download complete!"}

