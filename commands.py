import asyncio
from utils import Logger, Config

class CommandHandler:
    def __init__(self, music_player, queue, icecast, youtube, config):
        self.music_player = music_player
        self.queue = queue
        self.icecast = icecast
        self.youtube = youtube
        self.config = config
        self.cooldowns = {}
        self.admins = set(config.admins)

    async def run(self):
        from highrise import Highrise, HighriseEvent
        self.bot = Highrise(token=self.config.highrise_token)
        await self.bot.connect()
        Logger.info("Connected to Highrise room.")
        async for event in self.bot.listen():
            if isinstance(event, HighriseEvent.Chat):
                user = event.user_id
                message = event.message
                await self.handle_message(user, message)

    async def handle_message(self, user, message):
        try:
            if not message.startswith("!"):
                return
            # Anti-spam: ignore repeated commands within 2s
            import time
            now = time.time()
            last = self.cooldowns.get(user, 0)
            if now - last < 2:
                Logger.info(f"Spam detected from {user}")
                return
            self.cooldowns[user] = now
            args = message[1:].split()
            if not args:
                return
            cmd = args[0].lower()
            params = args[1:]
            # Admin-only commands
            admin_cmds = {"stop", "clear", "remove"}
            if cmd in admin_cmds and user not in self.admins:
                Logger.info(f"Unauthorized admin command: {cmd} by {user}")
                return
            if cmd == "play" and params:
                await self.music_player.play_command(user, " ".join(params))
            elif cmd == "skip":
                await self.music_player.skip_command(user)
            elif cmd == "stop":
                await self.music_player.stop_command(user)
            elif cmd == "pause":
                await self.music_player.pause_command(user)
            elif cmd == "resume":
                await self.music_player.resume_command(user)
            elif cmd == "queue":
                await self.queue.show_queue(user)
            elif cmd == "nowplaying":
                await self.music_player.now_playing(user)
            elif cmd == "volume" and params:
                await self.music_player.set_volume(user, params[0])
            elif cmd == "loop":
                await self.queue.toggle_loop(user)
            elif cmd == "clear":
                await self.queue.clear(user)
            elif cmd == "remove" and params:
                await self.queue.remove_song(user, params[0])
            else:
                Logger.info(f"Unknown command: {cmd}")
        except Exception as e:
            Logger.error(f"Command error: {e}")
