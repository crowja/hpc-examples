#! /usr/bin/env python3

"""Tasks farmed out to a pool of processes."""

# 23456789 123456789 123456789 123456789 123456789 123456789 123456789 123456789
"""
A pool of processes is set up and tasks are farmed out to it. After a process
completes its work, it's assigned the next task.

Here each task to perform is represented as a Task. 

In this example, the analysis performed by analysis() sets the result, and the
updated object is returned.
"""

from multiprocessing import Pool, TimeoutError
import os
import time


class Task:
    def __init__(self):
        self.i = False
        self.j = False
        self.result = False

    def set_params(self, i, j):
        self.i = i
        self.j = j


def analysis(x):
    print("==")
    print(f"working in mypid={os.getpid()} with vals {x.i} and {x.j}")
    time.sleep(3)
    x.result = os.getpid()  # update task with a result
    return x


if __name__ == "__main__":

    # Create a task list, each task object representing a set of parameters
    # to be used as the argument of a call to analysis() above.
    tasks = []
    for i in range(10):
        task = Task()
        task.set_params(i, i + 1)
        tasks.append(task)

    # Set up a pool of processes and let the pool work through the task list.
    # It seems the default for Pool() is one process per CPU. I don't know yet
    # if this somehow leads to conflicts when multithreading in a VCPU ...
    ##with Pool(processes=2) as pool:
    with Pool() as pool:
        completed_tasks = pool.map(analysis, tasks)

    print("==")
    for task in completed_tasks:
        print(f"{task.i}\t{task.j}\t{task.result}")

    # Thought this would print out the same stuff as above, but it doesn't.

    print("==")
    for task in tasks:
        print(f"{task.i}\t{task.j}\t{task.result}")
