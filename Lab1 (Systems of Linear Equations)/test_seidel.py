from unittest import TestCase
from seidel_method import Seidel
import numpy as np

class TestSeidel(TestCase):
    def test_Seidel_10(self):
        self.assertEqual(Seidel(3, 0.01, np.array([[1, 4, 4], [1, -2, -2], [1, 1, 2]]), np.array([-15, 9, -4])),
                         "The solution is divergent. This method is not suitable for solving the current example")

    def test_Seidel_20(self):
        self.assertEqual(Seidel(3, 0.01, np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), np.array([0, 0, 0])),
                         "This method is not suitable for solving the current example")

    def test_Seidel_30(self):
        self.assertEqual(Seidel(3, 0.01, np.array([[10, 1, 1], [2, 10, 1], [2, 2, 10]]), np.array([12, 13, 14])),
                         (1.0002959, 1.00001144, 0.99993853))

    def test_Seidel_40(self):
        self.assertEqual(Seidel(4, 0.01, np.array([[8, -11, 1, 4], [1, 2, 3, 3], [7, 5, 2, -5], [2, 7, 4, 1]]), np.array([0, 0, 0, 0])),
                         (0, 0, 0, 0))

    def test_Seidel_50(self):
        self.assertEqual(Seidel(3, 0.01, np.array([[7, 1, -2], [0, 0, 0], [3, 1, 1]]), np.array([-15, 2, 3])),
                         "This method is not suitable for solving the current example")