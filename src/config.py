"""環境変数などの定数を返す関数を提供するモジュール"""
import os
from dotenv import load_dotenv

load_dotenv()


def DISCORD_TOKEN() -> str:
    return os.getenv("DISCORD_TOKEN")


def DATABASE_NAME() -> str:
    return ".db"
