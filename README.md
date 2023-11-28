# Priority Queue Task

## Introduction
This is the repository for the Priority Queue Task

### Task description:
* Requires a task queue with priorities and resource limits.
* Each task has a priority and the required amount of resources to process it.
* Publishers create tasks with specified resource limits, and put them in a task queue.
* Consumer receives the highest priority task that satisfies available resources.
* The queue is expected to contain thousands of tasks.
* Write a unit test to demonstrate the operation of the queue.

### Solution 
I have used uses a min-heap to maintain the tasks in the queue based on their priorities. A priority queue is common use for a 
[heap](https://docs.python.org/3/library/heapq.html). The `get_task` method checks for tasks that have sufficient resources and returns the task with the highest priority. The unit test demonstrates the functionality of the task queue. 

## Prerequisites
Before setting up the project, ensure you have the following installed:
- Python 3.12
- Git

## Setup
To set up the development environment for the project, follow these steps:

1. Clone the repository:
```git clone https://github.com/babujyan/task_queue.git```
2. Navigate to the project directory:
```cd path_to_repo```
3. Run the Makefile to create a virtual environment, install dependencies and to set up the pre-commit hook:
```make```

This will create a virtual environment and install necessary dependencies.

- **Running Tests:**
```make test```
This command runs all unit tests.

- **Linting the Code:**
```make lint```
This command will check if the code follows the formatting standards set by Black.

- **Formatting Code:**
```make format```
Automatically formats your code according to Black's formatting standards.

## Pre-commit Hook
A pre-commit hook is set up to run linting and tests before each commit:
It ensures that code formatting (via Black) and unit tests are checked before every commit.

