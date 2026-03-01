import asyncio
from utils import Logger

class SongQueue:
    def __init__(self):
        self.queue = []
        self.loop = False

    def add_song(self, song):
        self.queue.append(song)
        Logger.info(f"Added to queue: {song['title']}")

    def skip_song(self):
        if self.queue:
            skipped = self.queue.pop(0)
            Logger.info(f"Skipped: {skipped['title']}")

    def clear(self, user=None):
        self.queue.clear()
        Logger.info("Queue cleared.")

    def remove_song(self, user, index):
        try:
            idx = int(index) - 1
            removed = self.queue.pop(idx)
            Logger.info(f"Removed from queue: {removed['title']}")
        except Exception as e:
            Logger.error(f"Remove failed: {e}")

    def toggle_loop(self, user=None):
        self.loop = not self.loop
        Logger.info(f"Loop mode: {'ON' if self.loop else 'OFF'}")

    def show_queue(self, user=None):
        if not self.queue:
            Logger.info("Queue is empty.")
            return
        for i, song in enumerate(self.queue, 1):
            Logger.info(f"{i}. {song['title']}")
