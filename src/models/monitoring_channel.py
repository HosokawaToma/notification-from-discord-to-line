"""MonitoringChannelクラスとデータベースとの連携を提供するモジュール"""
import sqlite3
import database

class MonitoringChannel:
    """新しいメッセージがあるか監視するDiscordのチャンネルを管理するクラス。"""

    def __init__(self, discord_grid_id: str, discord_channel_id: str):
        self.discord_grid_id = discord_grid_id
        self.discord_channel_id = discord_channel_id

    def __repr__(self):
        return f"MonitoringChannel(discord_grid_id='{self.discord_grid_id}', discord_channel_id='{self.discord_channel_id}')"

    @staticmethod
    def create_table():
        """データベースとテーブルを作成（初回のみ）"""
        database.execute_query("""
        CREATE TABLE IF NOT EXISTS monitoring_channels (
            discord_grid_id TEXT NOT NULL,
            discord_channel_id TEXT NOT NULL,
            PRIMARY KEY (discord_grid_id, discord_channel_id)
        )
        """)

    @classmethod
    def create(cls, discord_grid_id: str, discord_channel_id: str):
        """新しい監視チャンネルを登録"""
        try:
            database.execute_query(
                "INSERT INTO monitoring_channels (discord_grid_id, discord_channel_id) VALUES (?, ?)",
                (discord_grid_id, discord_channel_id)
            )
            return cls(discord_grid_id, discord_channel_id)
        except sqlite3.IntegrityError:
            print("Error: このチャンネルは既に存在します")
            return None

    @classmethod
    def get_all(cls):
        """すべての監視チャンネルを取得"""
        rows = database.fetch_query("SELECT * FROM monitoring_channels")
        return [cls(*row) for row in rows]

    def delete(self):
        """特定の監視チャンネルを削除"""
        database.execute_query(
            "DELETE FROM monitoring_channels WHERE discord_grid_id = ? AND discord_channel_id = ?",
            (self.discord_grid_id, self.discord_channel_id)
        )
