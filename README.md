# Highrise Music Bot

A production-ready async music bot for Highrise radio using Icecast and FFmpeg.

## Installation

1. Install Python 3.10+
2. Install dependencies:
   ```
   pip install yt-dlp python-dotenv aiohttp requests highrise-sdk
   ```
3. Install FFmpeg and ensure it's in your PATH.
4. Start your Icecast server and configure mountpoint.
5. Copy `.env.example` to `.env` and fill in your credentials:
   - ICECAST_URL
   - ICECAST_USER
   - ICECAST_PASS
   - ADMINS
   - FFMPEG_PATH
   - YOUTUBE_API_KEY
   - HIGHRISE_TOKEN

## Example FFmpeg Command
```
ffmpeg -re -i <audio_url> -vn -c:a libmp3lame -b:a 192k -f mp3 icecast://source:password@localhost:8000/live
```

## Example Icecast Configuration
- Set up a mountpoint `/live` with source password.
- Allow MP3 streaming.

## Usage
1. Run the bot:
   ```
   python bot/main.py
   ```
2. Join your Highrise room and type commands:
   - `!play songname`
   - `!skip`
   - `!stop`
   - `!pause`
   - `!resume`
   - `!queue`
   - `!nowplaying`
   - `!volume 0-100`
   - `!loop`
   - `!clear`
   - `!remove number`

## Features
- Async, low-latency music streaming
- Multi-user queue and voting
- Admin-only commands
- Cooldown and anti-spam
- Auto-reconnect and error logging
- Graceful shutdown

## Troubleshooting
- Ensure Icecast and FFmpeg are running and configured
- Check `.env` for correct credentials
- Review logs for errors

## Testing
- Try all commands in your Highrise room
- Confirm song starts within 2–3 seconds
- Check queue, skip, and admin features

---
For advanced customization or persistent queue storage, contact the developer.
