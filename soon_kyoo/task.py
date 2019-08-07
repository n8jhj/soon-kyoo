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
            raise ValueError('task_name should be set')
        self.broker = Broker()

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        # Subclasses should implement their run logic here.
        raise NotImplementedError('Task run method must be implemented.')

    def delay(self, *args, **kwargs):
        try:
            task_id = str(uuid.uuid4())
            _task = {'task_id': task_id, 'args': args, 'kwargs': kwargs}
            serialized_task = json.dumps(_task)
            self.broker.enqueue(queue_name=self.task_name, item=serialized_task)
            print(f'Task {task_id} succesfully queued.')
        except Exception:
            raise Exception('Unable to publish task to the broker.')  
