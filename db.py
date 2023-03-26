import os
import json
from urllib.parse import urlparse

import psycopg2

from openaiHandler import queryImage

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


def insertAction(action, actor, game_id=None):
    game_id = game_id or createGameId()
    insert_query = """INSERT INTO actions
                      (action, actor, game_id) 
                      VALUES (%s, %s, %s)
                      RETURNING action_id"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(insert_query, (json.dumps(action), actor, game_id))
    generated_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return game_id, generated_id


def getActions(game_id):
    select_query = """SELECT * from actions
                   where game_id = %s
                   ORDER BY created_at ASC
                   LIMIT 10"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(select_query, (game_id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()

    result = []
    for row in rows:
        result.append({"content": row[2], "actor": row[3]})
    return result


def insertImage(image: bytes, game_id):
    insert_query = """INSERT INTO images
                      (image, game_id)
                      VALUES (%s, %s)
                      RETURNING image_id"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        insert_query, (psycopg2.Binary(image), game_id)
    )
    generated_id = cur.fetchone()[0] 
    conn.commit()
    cur.close()
    conn.close()
    return generated_id 


def getImage(image_id):
    select_query = """SELECT * from images
                   where image_id = %s"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(select_query, (image_id,))
    result = bytes(cur.fetchone()[3]) if cur.rowcount else None
    cur.close()
    conn.close()
    return result


if __name__ == "__main__":
    # TESTING ACTIONS/GAME ID
    action = ['foo', {'bar': ('baz', None, 1.0, 2)}]
    game_id, action_id = insertAction(action, None)
    print(game_id, action_id)
    print(getActions(game_id))
    
    # TESTING IMAGES
    IMG_PATH = "../4HackathonFrontend/public/logo192.png"
    with open(IMG_PATH, "rb") as f:
        im = f.read()
    print('im', im)
    image_id = insertImage(im, game_id)
    print('im id', image_id)
    im2 = getImage(image_id)
    print('im2', im2)
    print('equal', im == im2)