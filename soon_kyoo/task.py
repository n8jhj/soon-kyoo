"""Implements task classes.

Defines:
BaseTask - Base task class.
"""

import abc
import json
import uuid

from .broker import Broker


class BaseTask(abc.ABC):
    """Base task class.

    Example Usage:
        class AdderTask(BaseTask):
            task_name = 'AdderTask'
            def run(self, a, b):
                result = a + b
                return result

        adder = AdderTask()
        adder.delay(9, 34)
    """

    task_name = None

    def __init__(self):
        if not self.task_name:
            raise ValueError("Class attribute 'task_name' should be set.")
        self.broker = Broker()
        # Status options:
        # detached - Instantiated, not queued.
        # queued - Queued via Broker.
        # running - Running via Worker.
        # complete - Run complete.
        self.status = 'detached'

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        # Subclasses should implement their run logic here.
        raise NotImplementedError('Task run method must be implemented.')

    def delay(self, *args, **kwargs):
        try:
            task_id = str(uuid.uuid4())
            task = {'task_id': task_id, 'args': args, 'kwargs': kwargs}
            serialized_task = json.dumps(task)
            self.broker.enqueue(
                queue_name=self.task_name, item=serialized_task)
            self.status = 'queued'
            print(f'Task {task_id} succesfully queued.')
        except Exception:
            raise Exception(f'Unable to publish task {task_id} to the broker.')  
    
    def __repr__(self):
        return (f"{self.__class__.__name__}({self.status})")
