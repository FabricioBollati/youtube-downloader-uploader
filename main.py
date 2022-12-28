import pytube
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import json


# Extract the client ID, client secret, and refresh token from the credentials
client_id = "Your Client ID"
client_secret = "Your Client Secret ID"
refresh_token = "Your Refresh Token"

# Obtain the YouTube video URL
video_url = "https://www.youtube.com/watch?v=EVOXouB3ktI"

# Download the YouTube video
yt = pytube.YouTube(video_url)
stream = yt.streams.get_highest_resolution()
stream.download()

# Authenticate with the Google API
creds = Credentials.from_authorized_user_info(info={
    "client_id": client_id,
    "client_secret": client_secret,
    "refresh_token": refresh_token
})

# Upload the YouTube video
service = build("youtube", "v3", credentials=creds)

try:
    request = service.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "My video",
                "description": "This is my video",
                "tags": ["cool", "video"],
                "categoryId": 22,
            },
            "status": {"privacyStatus": "private"},
        },
        media_body=f"{yt.title}.mp4",
    )
    response = request.execute()

    print(f"Video uploaded: {response['id']}")
except HttpError as error:
    print(f"An error occurred: {error}")
    response = None