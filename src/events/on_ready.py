"""discord bot のon_readyイベントの処理を提供するモジュール"""
from models import User, MonitoringChannel

def on_ready():
    """discord bot のon_readyイベントの処理"""
    User.create_table()
    MonitoringChannel.create_table()
    return
