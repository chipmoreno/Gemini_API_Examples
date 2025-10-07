from google import genai
from google.genai import types
import json
from PIL import Image
from IPython.display import display, Markdown, HTML
import os
from dotenv import load_dotenv
import time

load_dotenv(override=True) 
api_key = os.getenv("GEMINI_API_KEY") 
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def upload_video(video_file_name):
  video_file = client.files.upload(file=video_file_name)
  print(f'Video processing complete: ' + video_file.uri)
  return video_file

trailcam_video = upload_video('Trailcam.mp4')

prompt = "For each scene in this video, generate captions that describe the scene along with any spoken text placed in quotation marks." \
" Place each caption into an object with the timecode of the caption in the video."  
video = trailcam_video 

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=[
        video,
        prompt,
    ]
)
print(response.text)    