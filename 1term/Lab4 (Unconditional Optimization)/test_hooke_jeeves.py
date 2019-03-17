from unittest import TestCase
from hooke_jeeves_method import hooke_jeeves
import numpy as np


class TestHooke_jeeves(TestCase):
    def test_hooke_jeeves_10(self):
        for i in range(2):
            self.assertEqual(hooke_jeeves(np.array([7, 6]), np.array([0.6, 0.8]), 0.001, 2)[i], 0)

    def test_hooke_jeeves_20(self):
        for i in range(2):
            self.assertEqual(hooke_jeeves(np.array([0, 0]), np.array([0.6, 0.8]), 0.000001, 2)[i], 0)

    def test_hooke_jeeves_30(self):
        for i in range(2):
            self.assertEqual(hooke_jeeves(np.array([1, 1]), np.array([0.01, 0.01]), 0.001, 2)[i], 0)

    def test_hooke_jeeves_40(self):
        for i in range(2):
            self.assertEqual(hooke_jeeves(np.array([0, 0]), np.array([0, 0]), 0.1, 2)[i], 0)

    def test_hooke_jeeves_50(self):
        for i in range(2):
            self.assertEqual(hooke_jeeves(np.array([-200, -200]), np.array([0.1, 0.1]), 0.001, 20)[i], 0)

    def test_hooke_jeeves_60(self):
        for i in range(2):
            self.assertEqual(hooke_jeeves(np.array([-2000, -2000]), np.array([0.8, 0.8]), 0.001, 2000)[i], 16)