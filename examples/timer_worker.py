"""Script for runnning a Worker dedicated to accomplishing TimerTasks.
"""

import soon_kyoo as sk

from timer_task import TimerTask


if __name__ == "__main__":
    # Instantiate TimerTask.
    timer_task = TimerTask()

    # Run worker.
    worker = sk.Worker(task=timer_task)
    worker.start()
