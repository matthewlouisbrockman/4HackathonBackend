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


def createGameId():
    insert_query = """INSERT INTO games
                   DEFAULT VALUES
                   RETURNING id"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(insert_query)
    generated_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return generated_id


def insertAction(action, game_id):
    game_id = game_id or createGameId()
    insert_query = """INSERT INTO actions
                   (action_id, created_at, action, actor, game_id)
                   VALUES
                   (%s, %s, %s, %s, %s)"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(insert_query, (game_id,))
    conn.commit()
    cur.close()
    conn.close()


def getActions(game_id):
    select_query = """SELECTION * from actions
                   where game_id = %s
                   ORDER BY created_at DESCENDING
                   LIMIT 10"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(select_query, (game_id,))
    rows = cur.fetch()
    cur.close()
    conn.close() 
    return rows


if __name__ == "__main__":
    # TESTING
    action = 
    print(createGameId())