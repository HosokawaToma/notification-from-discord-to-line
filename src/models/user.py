"""Userクラスとデータベースとの連携を提供するモジュール"""
import pymysql
import database

class User:
    """DiscordアカウントとLINEアカウントのIDを管理するクラス。"""

    def __init__(self, discord_user_id: str, line_user_id: str):
        self.discord_user_id = discord_user_id
        self.line_user_id = line_user_id

    @staticmethod
    def create_table():
        """テーブルを作成（初回のみ）"""
        database.execute_query("""
        CREATE TABLE IF NOT EXISTS users (
            discord_user_id VARCHAR(255) PRIMARY KEY,
            line_user_id VARCHAR(255) UNIQUE NOT NULL
        )
        """)

    @classmethod
    def create(cls, discord_user_id: str, line_user_id: str):
        """新しいユーザーを登録"""
        try:
            database.execute_query(
                "INSERT INTO users (discord_user_id, line_user_id) VALUES (%s, %s)",
                (discord_user_id, line_user_id)
            )
            return cls(discord_user_id, line_user_id)
        except pymysql.err.IntegrityError:
            print("Error: このユーザーは既に存在します")
            return None

    @classmethod
    def get_all(cls):
        """すべてのユーザーを取得"""
        rows = database.fetch_query("SELECT * FROM users")
        return [cls(**row) for row in rows]

    def delete(self):
        """ユーザーを削除"""
        database.execute_query(
            "DELETE FROM users WHERE discord_user_id = %s AND line_user_id = %s",
            (self.discord_user_id, self.line_user_id)
        )
