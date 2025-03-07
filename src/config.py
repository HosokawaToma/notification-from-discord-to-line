from dotenv import load_dotenv
import os

load_dotenv()

def DISCORD_TOKEN() -> str:
    return os.getenv("DISCORD_TOKEN")
