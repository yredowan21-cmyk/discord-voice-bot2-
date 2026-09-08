import os
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing. Put your bot token in the .env file.")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Slash commands synced.")


@bot.tree.command(name="join", description="Join a voice channel")
@app_commands.describe(channel="Choose the voice channel to join")
async def join(interaction: discord.Interaction, channel: discord.VoiceChannel):
    if interaction.guild is None:
        await interaction.response.send_message(
            "This command can only be used inside a server.",
            ephemeral=True,
        )
        return

    try:
        voice = interaction.guild.voice_client

        if voice:
            await voice.move_to(channel)
        else:
            await channel.connect()

        await interaction.response.send_message(
            f"🔊 Joined **{channel.name}**"
        )

    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ I need Connect/Speak permission for that voice channel.",
            ephemeral=True,
        )
    except discord.HTTPException:
        await interaction.response.send_message(
            "❌ Discord returned an error while connecting.",
            ephemeral=True,
        )


@bot.tree.command(name="leave", description="Leave the current voice channel")
async def leave(interaction: discord.Interaction):
    if interaction.guild is None:
        await interaction.response.send_message(
            "This command can only be used inside a server.",
            ephemeral=True,
        )
        return

    voice = interaction.guild.voice_client

    if voice is None:
        await interaction.response.send_message(
            "ℹ️ I'm not currently in a voice channel.",
            ephemeral=True,
        )
        return

    await voice.disconnect()
    await interaction.response.send_message("👋 Left the voice channel.")


bot.run(TOKEN)
