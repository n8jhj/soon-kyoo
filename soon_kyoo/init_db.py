"""Functionality for initializing the database.

Defines:
init_db
"""

import pathlib
import sqlite3


def init_db():
    here = pathlib.Path(__file__)
    db_path = here.parents[0] / 'instance' / 'queue.sqlite'
    conn = sqlite3.connect(db_path)
    with conn:
        conn.execute('''CREATE TABLE queue
            (id TEXT PRIMARY KEY NOT NULL, position INTEGER UNIQUE NOT NULL, name TEXT)''')
    conn.close()


if __name__ == '__main__':
    init_db()
