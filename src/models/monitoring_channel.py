"""MonitoringChannelクラスを提供するモジュール"""

class MonitoringChannel:
    """新しいメッセージがあるか監視するDiscordのチャンネルを管理するクラス。"""

    def __init__(self, discord_grid_id: str, discord_channel_id: str):
        self.discord_grid_id = discord_grid_id
        self.discord_channel_id = discord_channel_id

    def __repr__(self):
        return f"MonitoringChannel(discord_grid_id='{self.discord_grid_id}', discord_channel_id='{self.discord_channel_id}')"
