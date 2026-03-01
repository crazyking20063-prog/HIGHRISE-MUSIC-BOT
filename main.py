import asyncio
import os
from dotenv import load_dotenv
from commands import CommandHandler
from music import MusicPlayer
from icecast import IcecastStreamer
from youtube import YouTubeClient
from queue import SongQueue
from utils import Logger, Config

load_dotenv()
ROOM_ID = os.getenv("ROOM_ID")
HIGHRISE_TOKEN = os.getenv("HIGHRISE_TOKEN")

async def main():
    Logger.info("Starting Highrise Music Bot...")
    config = Config.load()
    queue = SongQueue()
    music_player = MusicPlayer(queue, config)
    icecast = IcecastStreamer(config)
    youtube = YouTubeClient(config)
    commands = CommandHandler(music_player, queue, icecast, youtube, config)
    # Connect to Highrise using SDK
    from highrise import __main__
    await __main__.run_bot(commands, ROOM_ID, HIGHRISE_TOKEN)

if __name__ == "__main__":
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        Logger.info("Bot shutdown requested.")
        # Graceful shutdown logic here
