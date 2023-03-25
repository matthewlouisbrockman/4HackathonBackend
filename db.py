import os
from urllib.parse import urlparse

import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")
URL_PARSED = urlparse(DATABASE_URL)


def get_connection():
    return psycopg2.connect(
        host=URL_PARSED.hostname,
        database=URL_PARSED.path[1:],
        user=URL_PARSED.username,
        password=URL_PARSED.password,
    )


def insertAction(action, game_id):
    insert_query = f"INSERT INTO actions " \
                   f"(action_id, created_at, action, actor, game_id) " \
                   f"VALUES " \
                   f"(%s, %s, %s, %s, %s)"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(insert_query, (*action, game_id))
    conn.commit()
    cur.close()
    conn.close()


def getAction(action_id):
    select_query = f"SELECTION * from actions " \
                   f"where game_id = %s"
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(select_query, (action_id,))
    row = cur.fetchone()
    cur.close()
    conn.close() 
    return row