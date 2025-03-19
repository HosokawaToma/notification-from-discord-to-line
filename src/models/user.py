"""Userクラスとデータベースとの連携を提供するモジュール"""
import sqlite3
import database

class User:
    """DiscordアカウントとLINEアカウントのIDを管理するクラス。"""

    def __init__(self, discord_user_id: str, line_user_id: str):
        self.discord_user_id = discord_user_id
        self.line_user_id = line_user_id

    def __repr__(self):
        return f"User(discord_user_id='{self.discord_user_id}', line_user_id='{self.line_user_id}')"

    @staticmethod
    def create_table():
        """データベースとテーブルを作成（初回のみ）"""
        database.execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            discord_user_id TEXT PRIMARY KEY,
            line_user_id TEXT UNIQUE NOT NULL
        )
        """)

    @classmethod
    def create(cls, discord_user_id: str, line_user_id: str):
        """新しいユーザーを登録"""
        try:
            database.execute_query(
                "INSERT INTO users (discord_user_id, line_user_id) VALUES (?, ?)",
                (discord_user_id, line_user_id)
            )
            return cls(discord_user_id, line_user_id)
        except sqlite3.IntegrityError:
            print("Error: このユーザーは既に存在します")
            return None

    @classmethod
    def get_all(cls):
        """すべてのユーザーを取得"""
        rows = database.fetch_query("SELECT * FROM users")
        return [cls(*row) for row in rows]

    def delete(self):
        """ユーザーを削除（discord_user_id と line_user_id の両方を指定）"""
        database.execute_query(
            "DELETE FROM users WHERE discord_user_id = ? AND line_user_id = ?",
            (self.discord_user_id, self.line_user_id)
        )
