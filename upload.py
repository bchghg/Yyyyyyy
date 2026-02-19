import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def upload():
    # استخدام ملف الـ JSON الذي قمت بتحميله
    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
    credentials = flow.run_console() 
    
    youtube = build('youtube', 'v3', credentials=credentials)
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": os.getenv('NAME'),
                "description": "Uploaded via Auto Smart Upload"
            },
            "status": {
                "privacyStatus": "unlisted"  # هنا جعلنا الفيديو غير مدرج
            }
        },
        media_body=MediaFileUpload("video.mp4", chunksize=-1, resumable=True)
    )
    response = request.execute()
    print(f"Done! Video ID: {response.get('id')}")

if __name__ == "__main__":
    upload()
