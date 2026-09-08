DISCORD VOICE BOT

Features
--------
/join  -> choose a voice channel; the bot joins it.
/leave -> the bot leaves the current voice channel.

SETUP
-----
1. Install Python 3.10+.
2. Open a terminal in this folder.
3. Install packages:
   pip install -r requirements.txt

4. Rename ".env.example" to ".env".
5. Open .env and put your Discord bot token:
   DISCORD_TOKEN=YOUR_TOKEN_HERE

6. Run:
   python bot.py

DISCORD DEVELOPER PORTAL
------------------------
Create an application at the Discord Developer Portal.
Add a Bot user and copy its token into .env.

When generating the install/invite link, enable these scopes:
- bot
- applications.commands

The bot needs permission to:
- View Channel
- Connect
- Speak (not required just to join, but useful if you later add audio)

IMPORTANT
---------
Never share your bot token. If it is exposed, reset it immediately in the
Discord Developer Portal.

USAGE
-----
In your server:
 /join -> pick a voice channel from the dropdown
 /leave -> leave voice

If slash commands do not appear immediately, wait a little and restart the bot.
