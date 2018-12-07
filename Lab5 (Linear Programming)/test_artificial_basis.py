from unittest import TestCase
from artificial_basis_method import artificial_basis
import numpy as np

class TestArtificial_basis(TestCase):
    def test_artificial_basis_10(self):
        self.assertEqual(artificial_basis([[240, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [150, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                                           [150, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                           [3, 30, 60, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                           [15, 0, 0, 0, 50, 100, 30, 0, 0, 0, 0, 0, 0],
                                           [4.5, 0, 0, 0, 0, 0, 0, 30, 60, 18, 0, 0, 0],
                                           [1.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 12],
                                           [0, -2, -1, -0.5, -1.2, -0.8, -1.2, -0.9, -0.8, -0.5, -1, -0.6, -0.9],
                                           [24, 30, 60, 18, 50, 100, 30, 30, 60, 18, 20, 40, 12]], 3, 4, 13), 0)

    def test_artificial_basis_20(self):
        self.assertEqual(artificial_basis([[1, 2, 3], [0, 4, 6], [7, 3 ,8]], 3, 4, 13), 0)