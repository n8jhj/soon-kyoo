"""Script for running a timer task.
"""

import time

import soon_kyoo as sk

from timer_function import timer_sleep_all


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
