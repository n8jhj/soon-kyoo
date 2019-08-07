"""Script for running a timer task.
"""

import time

from soon_kyoo.task import BaseTask


class TimerTask(BaseTask):
    """Task to count to a certain number a certain number of times.
    """

    task_name = 'TimerTask'

    def run(self, interval, n):
        """Count at the given interval the given number of times.

        Positional arguments:
        interval - (int) Interval, in seconds.
        n - (int) Number of times to count the given interval.
        """
        for i in range(n):
            now = time.strftime()
            print(f'{i}/{n} -- {now} -- Sleeping for {interval} seconds.')
            time.sleep(interval)
        print(f'Slept {interval * n} seconds total.')


if __name__ == '__main__':
    timer_task = TimerTask()
    timer_task.run(5, 3)
