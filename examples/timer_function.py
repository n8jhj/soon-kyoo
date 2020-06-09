"""Implements timer functionality.
"""

import time

import soon_kyoo as sk


def timer_sleep_all(interval, n):
    for i in range(n):
        timer_sleep(interval, i, n)


def timer_sleep(interval, i=None, n=None):
    if None not in (i, n):
        msg = f"{i+1}/{n} "
    else:
        msg = ''
    msg += f"Sleeping {interval} seconds..."
    sk.echo(msg)
    time.sleep(interval)
