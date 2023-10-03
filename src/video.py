from src.channel import Channel
from googleapiclient.discovery import build
import os
class Video(Channel):
    def __init__(self, video_id):
        self.video_id = video_id
        try:
            self.video_response = super().get_service().videos().list(
                part='snippet,statistics,contentDetails,topicDetails',
                id=self.video_id
                ).execute()

            self.title = self.video_response['items'][0]['snippet']['title']
            self.video_url = f'https://www.youtube.com/video/{self.video_id}'
            self.views_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']
            self.duration = self.video_response['items'][0]['contentDetails']['duration']

        except IndexError:
            self.video_id = video_id
            self.video_response = None
            self.video_url = None
            self.title = None
            self.views_count = None
            self.like_count = None
            self.duration = None



    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id