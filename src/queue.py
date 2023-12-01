from dataclasses import dataclass
import heapq
from functools import total_ordering


@total_ordering
@dataclass
class Resources:
    """
    A class representing resources in terms of RAM, CPU cores, and GPU count.

    The class uses total_ordering to simplify comparison operations. It only defines
    __lt__ (less than) and __eq__ (equality) operations, and other comparison operations
    are automatically generated.
    """

    ram: int
    cpu_cores: int
    gpu_count: int

    def __lt__(self, other) -> bool:
        """
        Less than comparison based on RAM, CPU cores, and GPU count.
        Returns True if all attributes are less than or equal to those of 'other'.
        """
        return (
            self.ram <= other.ram
            and self.cpu_cores <= other.cpu_cores
            and self.gpu_count <= other.gpu_count
        )

    def __eq__(self, other) -> bool:
        """
        Equality comparison based on RAM, CPU cores, and GPU count.
        Returns True if all attributes are equal to those of 'other'.
        """
        return (
            self.ram == other.ram
            and self.cpu_cores == other.cpu_cores
            and self.gpu_count == other.gpu_count
        )


@total_ordering
@dataclass
class Task:
    """
    A class representing a task with an ID, priority, required resources, content, and result.

    The class also uses total_ordering for comparison operations based on task priority.
    """

    id: int  # Task identifier
    priority: int  # Task priority (higher number indicates higher priority)
    resources: Resources  # Required resources for the task
    content: str  # Task content
    result: str  # Result of the task

    def __lt__(self, other) -> bool:
        """
        Less than comparison based on priority.
        Returns True if the priority of the task is greater than that of 'other'.
        Note: Higher priority is represented by a higher number.
        """
        return self.priority > other.priority

    def __eq__(self, other) -> bool:
        """
        Equality comparison based on priority.
        Returns True if the priority of the task is equal to that of 'other'.
        """
        return self.priority == other.priority


class TaskQueue:
    """
    A class representing a priority queue for tasks.

    It uses a min-heap under the hood to store the tasks based on their priority.
    """

    def __init__(self):
        """
        Initializes the task queue with an empty list.
        """
        self.queue = []  # Internal list to store tasks

    def add_task(self, task: Task):
        """
        Adds a task to the queue.

        Uses heapq.heappush to add the task to the min-heap.
        """
        heapq.heappush(self.queue, task)

    def get_task(self, available_resources: Resources) -> Task:
        """
        Retrieves and removes a task from the queue that can be executed with the available resources.

        Iterates through the queue to find a task matching the resource criteria.
        Returns the first matching task or None if no match is found.
        """
        tasks_to_requeue = []
        found = False
        while self.queue:
            task = heapq.heappop(self.queue)
            if task.resources <= available_resources:
                found = True
                break
            else:
                tasks_to_requeue.append(task)

        for task_to_queue in tasks_to_requeue:
            self.add_task(task_to_queue)
        if found:
            return task
        else:
            return None
