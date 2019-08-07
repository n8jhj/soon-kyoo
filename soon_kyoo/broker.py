"""Implements broker classes.

Defines:
Broker
"""

import datetime as dt
import sqlite3

from soon_kyoo.db_config import db_path


class Broker:
    """Implements a basic FIFO queue using SQLite.
    """

    def enqueue(self, item, queue_name):
        con = sqlite3.connect(str(db_path))
        with con:
            c = con.execute(
                'SELECT position FROM queue ORDER BY position DESC')
            max_position = c.fetchone()
            new_position = max_position[0] + 1 if max_position else 0
            con.execute('INSERT INTO queue VALUES (?, ?, ?, ?, ?, ?)', (
                item['task_id'], queue_name, new_position, item['args'],
                item['kwargs'], dt.datetime.now(),
            ))

    def dequeue(self, queue_name):
        dequed_item = self.redis_instance.brpop(queue_name, timeout=3)
        if not dequed_item:
            return None
        dequed_item = dequed_item[1]
        return dequed_item
