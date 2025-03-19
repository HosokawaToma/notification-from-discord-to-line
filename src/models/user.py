"""Userクラスを提供するモジュール"""

class User:
    """DiscordアカウントとLINEアカウントのIDを管理するクラス。"""

    def __init__(self, discord_user_id: str, line_user_id: str):
        self.discord_user_id = discord_user_id
        self.line_user_id = line_user_id

    def __repr__(self):
        return f"User(discord_user_id='{self.discord_user_id}', line_user_id='{self.line_user_id}')"
