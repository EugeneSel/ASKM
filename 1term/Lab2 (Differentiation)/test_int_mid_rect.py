from unittest import TestCase
from integration_middle_rectagles_method import int_mid_rect

class TestInt_mid_rect(TestCase):
    def test_int_mid_rect_10(self):
        self.assertEqual(int_mid_rect(0, 0.9, 1000), 0.27163939357734845)

    def test_int_mid_rect_20(self):
        self.assertEqual(int_mid_rect(0, 0, 100000), 0)

    def test_int_mid_rect_30(self):
        self.assertEqual(int_mid_rect(0, 0.5, 10), 0.0426886755045163)

    def test_int_mid_rect_40(self):
        self.assertEqual(int_mid_rect(-1, 1, 1000), 0.7853822437404907)

    def test_int_mid_rect_50(self):
        self.assertEqual(int_mid_rect(-1, 0, 100000), 0.39269907896918677)

    def test_int_mid_rect_60(self):
        self.assertEqual(int_mid_rect(-1, -0.999999999, 10), 1.5707663905513454e-09)

    def test_int_mid_rect_70(self):
        self.assertEqual(int_mid_rect(0.999999999, 1, 10), 1.5707663905513454e-09)