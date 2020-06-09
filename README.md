# soon-kyoo
A subprocess-based task queue.

## Introduction
Soon-Kyoo implements a simple FIFO queue using SQLite. It was created primarily for running long simulations.

As of yet, the subprocess-based workflow has not been implemented. However, the package still works as a task queue.

## Usage

Users must create their own subclass of `soon_kyoo.BaseTask`. Subclasses must define a `run()` method, which contains the business logic for the task (what we care about). There are no restrictions on input arguments or return values.

## Example

    # timer_task.py

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
                now = time.strftime('%Y-%m-%d %H:%M:%S')
                print(f'{i+1}/{n} -- {now} -- Sleeping for {interval} seconds.')
                time.sleep(interval)
            print(f'Slept {interval * n} seconds total.')


    if __name__ == '__main__':
        # Create a new task.
        timer_task = TimerTask()

        # Add the task to the queue, to be executed at some future time.
        # Arguments to delay() are the same as for run().
        timer_task.delay(3, 3)


## Etymology
This project is named after my friend, Soon-Kyoo. People call him Q, for short.
