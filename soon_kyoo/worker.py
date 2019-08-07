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

    def start(self):
        while True:
            try:
                # Read database.
                _dequeued_item = self.task.broker.dequeue(
                    queue_name=self.task.task_name)
                dequeued_item = json.loads(_dequeued_item)
                task_id = dequeued_item['task_id']
                task_args = dequeued_item['args']
                task_kwargs = dequeued_item['kwargs']
                # Do run.
                print(f'Running task: {task_id}')
                self.task.run(*task_args, **task_kwargs)
                self.task.status = 'running'
                print(f'Succesful run of task: {task_id}')
            except Exception:
                print(f'Unable to execute task {self.task}.')
                continue       
