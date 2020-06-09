"""Implements worker classes.

Classes:
Worker
"""

import json

from .utils import echo


class Worker:
    """Basic worker class.

    Example Usage:
        task = AdderTask()
        worker = Worker(task=task)
        worker.start()
    """

    def __init__(self, task):
        self.task = task
        self.waiting = False

    def start(self):
        """Begin working on the assigned type of task."""
        while True:
            try:
                # Read database.
                dequeued_item = self.task.broker.dequeue(
                    queue_name=self.task.task_name)
                self.waiting = False
                self.task.set_status('dequeued')
                task_id, _, _, task_args, task_kwargs, _ = dequeued_item
                task_args = json.loads(task_args)
                task_kwargs = json.loads(task_kwargs)
                # Run.
                echo(f'Running task: {task_id}')
                self.task.set_status('running')
                self.task.run(*task_args, **task_kwargs)
                echo(f'Finished task: {task_id}')
                self.task.set_status('complete')
            except KeyboardInterrupt:
                echo('Quitting')
                break
            except Exception:
                if not self.waiting:
                    echo(f'Waiting for next task... (Ctrl + C to quit)')
                    self.waiting = True
                continue
