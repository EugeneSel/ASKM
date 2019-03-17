from unittest import TestCase
from artificial_basis_method import artificial_basis
import numpy as np

class TestArtificial_basis(TestCase):
    def test_artificial_basis_10(self):
        for i in range(12):
            if i >= 4 and i <= 7:
                answer = i
            else:
                answer = 0
            self.assertEqual(artificial_basis(np.array([[240, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                                        [150, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
                                                        [150, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
                                                        [3, 30, 0, 0, 0, 60, 0, 0, 0, 18, 0, 0, 0],
                                                        [15, 0, 50, 0, 0, 0, 100, 0, 0, 0, 30, 0, 0],
                                                        [4.5, 0, 0, 30, 0, 0, 0, 60, 0, 0, 0, 18, 0],
                                                        [1.5, 0, 0, 0, 20, 0, 0, 0, 40, 0, 0, 0, 12],
                                                        [0, -2, -1, -0.5, -1.2, -0.8, -1.2, -0.9, -0.8, -0.5, -1, -0.6, -0.9],
                                                        [24, 30, 50, 30, 20, 60, 100, 60, 40, 18, 30, 18, 12]]), 3, 4)[1][i], answer)

    def test_artificial_basis_20(self):
        for i in range(12):
            self.assertEqual(artificial_basis(np.zeros([9, 13]), 3, 4)[1][i], 0)

    def test_artificial_basis_30(self):
        for i in range(6):
            if i == 0:
                answer = 3
            elif i == 1:
                answer += i
            elif i == 2:
                answer -= i + 1
            elif i == 5:
                answer = i
            else:
                answer = 0
            self.assertEqual(artificial_basis(np.array([[60., 1., 1., 1., 0., 0., 0.],
                                                        [70., 0., 0., 0., 1., 1., 1.],
                                                        [160., 8., 0., 0., 4., 0., 0.],
                                                        [100., 0., 4., 0., 0., 2., 0.],
                                                        [100., 0., 0., 2., 0., 0., 1.],
                                                        [0., -4., -6., -3., -5., -4., -2.],
                                                        [360., 8., 4., 2., 4., 2., 1.]]), 2, 3)[1][i], answer)