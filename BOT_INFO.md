# Highrise Music Bot

This is a Python music bot for Highrise rooms. It can play songs, manage queues, and respond to chat commands. You can run it on Replit or locally.

## Features
- Play songs from YouTube using yt-dlp
- Queue management
- Icecast streaming support
- Highrise chat command integration

## How It Works
1. The bot connects to your Highrise room using your token and room ID.
2. Users send chat commands in Highrise to control music playback (play, skip, queue, etc).
3. The bot downloads songs from YouTube and streams them using Icecast.
4. The queue system manages song order and playback.

## Setup Instructions
### 1. Environment Variables
Create a `.env` file with these variables:
```
ROOM_ID=your_highrise_room_id
HIGHRISE_TOKEN=your_highrise_token
```

### 2. Install Dependencies
On Replit, add these to `requirements.txt`:
```
highrise-bot-sdk==24.1.0
yt-dlp
python-dotenv
```

### 3. Run the Bot
On Replit, set the entrypoint to `bot/main.py`.

## File Structure
- `bot/` - Main bot code
  - `main.py` - Entry point
  - `commands.py` - Chat command handling
  - `music.py` - Music playback logic
  - `queue.py` - Song queue management
  - `icecast.py` - Icecast streaming
  - `youtube.py` - YouTube download logic
  - `utils.py` - Utility functions
  - `README.md` - Bot usage info
- `.env` - Your secrets (not uploaded to GitHub)
- `requirements.txt` - Python dependencies

## How to Upload to GitHub
1. Do NOT upload your `.env` file (keep your secrets private).
2. Upload all files except `.env` to your GitHub repo.
3. On Replit, clone your repo and add your `.env` file manually.

## How to Run on Replit
1. Clone your GitHub repo in Replit.
2. Add your `.env` file with your ROOM_ID and HIGHRISE_TOKEN.
3. Install dependencies (Replit does this automatically from requirements.txt).
4. Run `bot/main.py`.

## Commands
- `!play <song name or link>`: Play a song
- `!skip`: Skip current song
- `!queue`: Show song queue
- `!stop`: Stop playback

## Troubleshooting
- If you see missing dependency errors, check your `requirements.txt`.
- If the bot can't connect, check your ROOM_ID and HIGHRISE_TOKEN in `.env`.

## License
MIT
