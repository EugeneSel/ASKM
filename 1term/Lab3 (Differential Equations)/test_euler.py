from unittest import TestCase
from euler_method import euler

class TestEuler(TestCase):
    def test_euler_10(self):
        self.assertEqual(euler(0.2, 0, 1, 0.1), (0.9999999999999999, 0.3522851585103483))

    def test_euler_20(self):
        self.assertEqual(euler(0, 0, 0, 0.1), (0, 0))

    def test_euler_30(self):
        self.assertEqual(euler(0, 0, -1, 0.1), (0.9999999999999999, 0.09117146625980643))

    def test_euler_40(self):
        self.assertEqual(euler(-5, 2.1, 0, 0.1), (4.200000000000001, 0.42884703254758155))

    def test_euler_50(self):
        self.assertEqual(euler(0, 0, 0.1, 0.0001), (0.10000000000000184, 0.0009990199006611853))