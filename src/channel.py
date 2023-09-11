import os
import json

from googleapiclient.discovery import build
class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.youtube = build('youtube', 'v3', developerKey=('AIzaSyBHKokX58L3gPhh7n7iIL2zpZ9JDHTKQwQ'))
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


