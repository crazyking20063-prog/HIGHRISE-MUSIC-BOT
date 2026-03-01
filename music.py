import asyncio
from utils import Logger

class MusicPlayer:
    def __init__(self, queue, config):
        self.queue = queue
        self.config = config
        self.current_song = None
        self.ffmpeg_process = None

    async def play_song(self, song):
        await self.stop()
        audio_url = song['audio_url']
        ffmpeg_cmd = [
            self.config.ffmpeg_path,
            '-re',
            '-i', audio_url,
            '-vn',
            '-c:a', 'libmp3lame',
            '-b:a', '192k',
            '-f', 'mp3',
            self.config.icecast_url
        ]
        try:
            self.ffmpeg_process = await asyncio.create_subprocess_exec(
                *ffmpeg_cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            Logger.info(f"Started streaming: {song['title']}")
        except Exception as e:
            Logger.error(f"FFmpeg start failed: {e}")
            # Auto-restart logic
            await asyncio.sleep(2)
            Logger.info("Retrying FFmpeg...")
            self.ffmpeg_process = await asyncio.create_subprocess_exec(
                *ffmpeg_cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )

    async def stop(self):
        if self.ffmpeg_process and self.ffmpeg_process.returncode is None:
            self.ffmpeg_process.terminate()
            await self.ffmpeg_process.wait()
            Logger.info("Stopped FFmpeg process.")
        self.ffmpeg_process = None

    async def skip(self):
        await self.stop()
        Logger.info("Song skipped.")

    async def play_command(self, user, query):
        # Search YouTube for the song
        from youtube import YouTubeClient
        youtube = YouTubeClient(self.config)
        results = await youtube.search(query)
        if not results:
            Logger.info(f"No results found for: {query}")
            return
        song = results[0]
        audio_url = await youtube.get_audio_url(song['id'])
        song['audio_url'] = audio_url
        self.queue.add_song(song)
        Logger.info(f"{user} requested: {song['title']}")
        self.current_song = song
        await self.play_song(song)

    async def skip_command(self, user):
        self.queue.skip_song()
        await self.skip()

    async def stop_command(self, user):
        await self.stop()

    async def pause_command(self, user):
        # FFmpeg pause not implemented, just log
        Logger.info("Pause requested (not implemented)")

    async def resume_command(self, user):
        # FFmpeg resume not implemented, just log
        Logger.info("Resume requested (not implemented)")

    async def now_playing(self, user):
        if self.current_song:
            Logger.info(f"Now playing: {self.current_song['title']}")
        else:
            Logger.info("No song is currently playing.")

    async def set_volume(self, user, volume):
        Logger.info(f"Volume set to: {volume} (not implemented)")
