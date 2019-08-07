"""Script that implements an e-commerce worker.
"""

from soon_kyoo.worker import Worker
from timer_task import TimerTask


if __name__ == "__main__":
    # Instantiate TimerTask.
    timer_task = TimerTask()
    # Run worker.
    worker = Worker(task=timer_task)
    worker.start()
