"""環境変数などの定数を返す関数を提供するモジュール"""
import os
from dotenv import load_dotenv

load_dotenv()


def DISCORD_TOKEN() -> str:
    return os.getenv("DISCORD_TOKEN")


def MYSQL_HOST() -> str:
    return "db"


def MYSQL_USER() -> str:
    return os.getenv("MYSQL_USER")


def MYSQL_PASSWORD() -> str:
    return os.getenv("MYSQL_PASSWORD")


def MYSQL_DATABASE() -> str:
    return os.getenv("MYSQL_DATABASE")


def MYSQL_PORT() -> str:
    return os.getenv("MYSQL_PORT")
