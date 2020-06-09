"""Implements task classes.

Classes:
BaseTask - Base task class.
"""

import abc
import json
import uuid

import click

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

    def __init__(self):
        self.broker = Broker()
        self.set_status('detached')

    @property
    @classmethod
    @abc.abstractmethod
    def task_name(cls):
        pass

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        """Subclasses must implement their business logic here."""
        pass

    def delay(self, *args, **kwargs):
        """Have the broker enqueue this task, thereby delaying its
        execution until some future time.
        """
        try:
            task_id = str(uuid.uuid4())
            task = dict(
                task_id=task_id,
                args=json.dumps(args),
                kwargs=json.dumps(kwargs),
            )
            self.broker.enqueue(
                item=task, queue_name=self.task_name)
            self.set_status('enqueued')
            click.echo(f'Queued task: {task_id}')
        except Exception:
            raise RuntimeError(
                f"Unable to publish task {task_id} to the broker.")

    def set_status(self, status):
        """Set status of the BaseTask instance. Options are:
        detached - Instantiated, not queued.
        enqueued - Queued via Broker.
        dequeued - Dequeued via Worker.
        running - Running via Worker.
        complete - Run complete.
        """
        if status not in (
                'detached', 'enqueued', 'dequeued', 'running', 'complete'):
            raise ValueError(f'Task status {status!r} not recognized.')
        self.status = status

    def __repr__(self):
        return (f"<{self.__class__.__name__}(status={self.status})>")
