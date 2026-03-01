import asyncio
from utils import Logger, Config

class YouTubeClient:
    def __init__(self, config):
        self.config = config

    async def search(self, query):
        import yt_dlp
        ydl_opts = {
            'quiet': True,
            'extract_flat': True,
            'default_search': 'ytsearch5',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(query, download=False)
            results = info.get('entries', [])
            # Smart matching: filter out live, shorts, low duration
            filtered = [r for r in results if not r.get('is_live') and r.get('duration', 0) > 60 and 'shorts' not in r.get('webpage_url', '')]
            return filtered[:5]

    async def get_audio_url(self, video_id):
        import yt_dlp
        ydl_opts = {
            'quiet': True,
            'format': 'bestaudio/best',
        }
        url = f'https://www.youtube.com/watch?v={video_id}'
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info['url']
