"""汎用的なデータベース処理用の関数を提供するモジュール"""
import pymysql
import config

def get_connection():
    """データベースの接続を取得"""
    return pymysql.connect(
        host=config.MYSQL_HOST(),
        user=config.MYSQL_USER(),
        password=config.MYSQL_PASSWORD(),
        database=config.MYSQL_DATABASE(),
        port=config.MYSQL_PORT(),
        cursorclass=pymysql.cursors.DictCursor
    )


def execute_query(sql, params=()):
    """データベースの更新系（INSERT, UPDATE, DELETE）"""
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        conn.commit()
    conn.close()


def fetch_query(sql, params=()):
    """データベースの取得系（SELECT）"""
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(sql, params)
        rows = cursor.fetchall()
    conn.close()
    return rows
