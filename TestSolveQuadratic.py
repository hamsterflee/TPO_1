import unittest
from main import solve_quadratic

class TestSolveQuadratic(unittest.TestCase):

    def test_two_real_roots(self):
        result = solve_quadratic(1, -3, 2)
        self.assertEqual(result, (2.0, 1.0))

    def test_one_real_root(self):
        result = solve_quadratic(1, -2, 1)
        self.assertEqual(result, (1.0,))

    def test_no_real_roots(self):
        result = solve_quadratic(1, 0, 1)
        self.assertIsNone(result)

    def test_a_is_zero(self):
        with self.assertRaises(ValueError) as context:
            solve_quadratic(0, 2, 1)
        self.assertEqual(str(context.exception), "Коэффициент 'a' не может быть нулевым.")

    def test_non_numeric_coefficients(self):
        with self.assertRaises(TypeError) as context:
            solve_quadratic('a', 2, 1)
        self.assertEqual(str(context.exception), "Коэффициенты должны быть числами.")

if __name__ == '__main__':
    unittest.main()
