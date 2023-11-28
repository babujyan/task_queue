import unittest
from src.queue import Resources


class TestResources(unittest.TestCase):
    def test_comparison_operators(self):
        resources1 = Resources(ram=4, cpu_cores=2, gpu_count=1)
        resources2 = Resources(ram=8, cpu_cores=2, gpu_count=1)
        resources3 = Resources(ram=8, cpu_cores=4, gpu_count=1)
        resources4 = Resources(ram=4, cpu_cores=2, gpu_count=1)

        self.assertTrue(resources1 < resources2)
        self.assertTrue(resources1 <= resources2)
        self.assertFalse(resources1 > resources2)
        self.assertFalse(resources1 >= resources2)
        self.assertTrue(resources1 == resources4)
        self.assertFalse(resources1 != resources4)
        self.assertTrue(resources2 < resources3)
        self.assertFalse(resources2 >= resources3)
