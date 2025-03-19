"""汎用的なデータベース処理用の関数を提供するモジュール"""
import sqlite3
import config


def execute_query(sql, parameters=()):
    """データベースの更新系（INSERT, UPDATE, DELETE）を実行"""
    conn = sqlite3.connect(config.DATABASE_NAME())
    cursor = conn.cursor()
    cursor.execute(sql, parameters)
    conn.commit()
    conn.close()


def fetch_query(sql, parameters=()):
    """データベースの取得系（SELECT）を実行し、結果を返す"""
    conn = sqlite3.connect(config.DATABASE_NAME())
    cursor = conn.cursor()
    cursor.execute(sql, parameters)
    rows = cursor.fetchall()
    conn.close()
    return rows
