"""Functionality for initializing the database.

Click commands:
init_db
"""

import sqlite3

import click

from soon_kyoo.db_config import db_path


@click.command()
def init_db():
    con = sqlite3.connect(str(db_path))
    # Create 'queue' table.
    table_name = 'queue'
    try:
        with con:
            con.execute(f'''CREATE TABLE {table_name}
                (task_id TEXT PRIMARY KEY NOT NULL,
                    position INTEGER UNIQUE NOT NULL,
                    published TIMESTAMP NOT NULL,
                    queue_name TEXT,
                    args TEXT,
                    kwargs TEXT)''')
        click.echo(f'Table {table_name!r} created.')
    except sqlite3.OperationalError:
        click.echo(f'Table {table_name!r} already exists.')
    # Create 'work' table.
    table_name = 'work'
    try:
        with con:
            con.execute(f'''CREATE TABLE {table_name}
                (task_id TEXT PRIMARY KEY NOT NULL,
                    started TIMESTAMP NOT NULL,
                    queue_name TEXT,
                    status TEXT)''')
        click.echo(f'Table {table_name!r} created.')
    except sqlite3.OperationalError:
        click.echo(f'Table {table_name!r} already exists.')
    # Close database connection.
    con.close()
