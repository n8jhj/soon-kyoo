"""Script for creating timer tasks.
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


class TimerTask(sk.BaseTask):
    """Task to count to a certain number a specified number of times.
    """

    task_name = 'TimerTask'

    def run(self, interval, n):
        """Count at the given interval the given number of times.

        Positional arguments:
        interval - (int) Interval, in seconds.
        n - (int) Number of times to count the given interval.
        """
        self.interval = interval
        timer_sleep_all(interval, n)
        sk.echo(f'Slept {interval * n} seconds total.')


if __name__ == '__main__':
    # Create a new task.
    timer_task = TimerTask()
    # Add the task to the queue, to be executed at some future time.
    # Arguments to delay() are the same as for run().
    timer_task.delay(3, 3)
