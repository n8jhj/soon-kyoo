# soon-kyoo
Simple queueing.

## Introduction
Implements a simple FIFO queue using SQLite.

## Usage

The user of soon-kyoo must create their own subclass of `soonkyoo.BaseTask`.
Subclasses must define a `run()` method, which contains the business logic for
the task (what we care about). There are no restrictions on input arguments or
return values.

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
