import unittest

import numpy as np

from qam_awgn_demo import square_qam_points


class SquareQAMPointsTests(unittest.TestCase):
    def test_supported_orders_have_expected_number_of_points(self):
        for order in (4, 16, 64, 256):
            with self.subTest(order=order):
                self.assertEqual(square_qam_points(order).shape, (order, 2))

    def test_constellation_is_normalized_and_symmetric(self):
        for order in (4, 16, 64, 256):
            with self.subTest(order=order):
                points = square_qam_points(order)
                self.assertLessEqual(float(np.max(np.abs(points))), 1.0)
                np.testing.assert_allclose(points.mean(axis=0), [0.0, 0.0], atol=1e-12)

    def test_non_square_modulation_order_is_rejected(self):
        with self.assertRaises(ValueError):
            square_qam_points(8)


if __name__ == "__main__":
    unittest.main()
