import unittest
from src.queue import Task
from src.queue import Resources


class TestTask(unittest.TestCase):
    def test_comparison_operators(self):
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

        # Comparison based on priority
        self.assertTrue(task1 > task2)
        self.assertTrue(task1 >= task2)
        self.assertFalse(task1 < task2)
        self.assertFalse(task1 <= task2)
        self.assertTrue(task1 == task3)
        self.assertFalse(task1 != task3)
