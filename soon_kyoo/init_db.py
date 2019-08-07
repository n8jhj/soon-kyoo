"""Functionality for initializing the database.

Defines:
init_db
"""

import sqlite3

from .db_config import db_path


def init_db():
    conn = sqlite3.connect(db_path)
    with conn:
        conn.execute('''CREATE TABLE queue
            (id TEXT PRIMARY KEY NOT NULL, position INTEGER UNIQUE NOT NULL, name TEXT)''')
    conn.close()


if __name__ == '__main__':
    init_db()
