"""Implements broker classes.

Classes:
Broker
"""

import datetime as dt
import sqlite3

from .config import db_path


class Broker:
    """Implements a basic FIFO queue using SQLite.
    """

    def enqueue(self, item, queue_name):
        """Enqueue the given item in the queue with the given name."""
        con = sqlite3.connect(str(db_path))
        with con:
            c = con.execute(
                '''
                SELECT position
                FROM queue
                ORDER BY position DESC
                '''
            )
            max_position = c.fetchone()  # Returns a tuple.
            new_position = max_position[0] + 1 if max_position else 0
            con.execute(
                '''
                INSERT INTO queue (
                    task_id,
                    queue_name,
                    position,
                    published,
                    args,
                    kwargs
                )
                VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (
                    item['task_id'], queue_name, new_position,
                    dt.datetime.now(), item['args'], item['kwargs'],
                )
            )
        con.close()

    def dequeue(self, queue_name):
        """Dequeue the next item (item with lowest position number) from
        the queue with the given name and return it.
        """
        con = sqlite3.connect(str(db_path))
        con.row_factory = sqlite3.Row
        with con:
            c = con.execute(
                f'''
                SELECT
                    task_id,
                    position,
                    published,
                    queue_name,
                    args,
                    kwargs
                FROM queue
                WHERE queue_name = {queue_name!r}
                ORDER BY position ASC
                '''
            )
            dequeued_item = c.fetchone()
            if dequeued_item:
                item_id = dequeued_item['task_id']
                c = con.execute(
                    f"DELETE FROM queue WHERE task_id = {item_id!r}")
        con.close()
        return dequeued_item
