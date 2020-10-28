#! /usr/bin/env python3

from multiprocessing import Pool, TimeoutError
import os
import time


class Task:
    def __init__(self):
        self.i = False
        self.j = False

    def set_params(self, i, j):
        self.i = i
        self.j = j


def analysis(x):
    print("==")
    print(f"working in mypid={os.getpid()} with vals {x.i} and {x.j}")
    time.sleep(3)
    return os.getpid()


if __name__ == "__main__":

    # Create a task list, each task object representing a set of parameters
    # to be used as the argument of a call to analysis() above.
    tasks = []
    for i in range(10):
        task = Task()
        task.set_params(i, i + 1)
        tasks.append(task)

    # Set up a pool of processes and let the pool work through the task list.
    ##with Pool(processes=2) as pool:
    with Pool() as pool:
        blah = pool.map(analysis, tasks)
        print(blah)
