"""Implements worker classes.

Defines:
Worker
"""

import json


class Worker:
    """Basic worker class.

    Example Usage:
        task = AdderTask()
        worker = Worker(task=task)
        worker.start()
    """
    def __init__(self, task):
        self.task = task
        self.working = False
        self.waiting = False

    def start(self):
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
                print(f'Running task: {task_id}')
                self.task.set_status('running')
                self.task.run(*task_args, **task_kwargs)
                print(f'Succesful run of task: {task_id}')
                self.task.set_status('complete')
            except Exception:
                if not self.waiting:
                    print(f'Waiting for next task...')
                    self.waiting = True
                continue
