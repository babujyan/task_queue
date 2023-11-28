import unittest
from src.queue import Task, Resources, TaskQueue


class TestTaskQueue(unittest.TestCase):
    def test_task_queue(self):
        task_queue = TaskQueue()

        task1 = Task(
            id=1,
            priority=1,
            resources=Resources(ram=4, cpu_cores=2, gpu_count=1),
            content="Task 1",
            result=None,
        )

        task2 = Task(
            id=2,
            priority=2,
            resources=Resources(ram=8, cpu_cores=4, gpu_count=2),
            content="Task 2",
            result=None,
        )

        task3 = Task(
            id=3,
            priority=1,
            resources=Resources(ram=4, cpu_cores=2, gpu_count=1),
            content="Task 3",
            result=None,
        )

        task4 = Task(
            id=4,
            priority=3,
            resources=Resources(ram=4, cpu_cores=2, gpu_count=3),
            content="Task 4",
            result=None,
        )

        available_resources = Resources(8, 4, 2)

        task_queue.add_task(task1)
        task_queue.add_task(task2)
        task_queue.add_task(task3)
        task_queue.add_task(task4)

        processed_task = task_queue.get_task(available_resources)

        self.assertIsNotNone(processed_task)
        # Task with highest priority and sufficient resources should be processed
        self.assertEqual(processed_task.id, 2)
