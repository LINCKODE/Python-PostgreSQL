# "Database code" for the DB Forum.


import datetime
import random

import psycopg2

CONNECTION_STRING = "dbname=forum user=postgres password=password host=localhost"


def get_posts():
    """Return all posts from the 'database', most recent first."""

    database = psycopg2.connect(CONNECTION_STRING)

    cursor = database.cursor()
    cursor.execute("select content, time, id from posts")
    data = cursor.fetchall()
    database.close()

    return reversed(data)


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""

    database = psycopg2.connect(CONNECTION_STRING)

    cursor = database.cursor()
    cursor.execute(
        "insert into posts values (%s, %s, %s)", (content, datetime.datetime.now(), random.randint(1, 10000000)))
    database.commit()

    database.close()


def remove_post(identification: str):
   
    database = psycopg2.connect(CONNECTION_STRING)

    cursor = database.cursor()
    cursor.execute(f"delete from posts") if identification == "ALL" else cursor.execute(f"delete from posts where id = {identification}")
    database.commit()

    database.close()
