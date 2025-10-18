import unittest
from Calc import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        cases = [((2, 3), 5), ((-1, 1), 0), ((0, 0), 0)]
        for (a, b), expect in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.add(a, b), expect)

    def test_sub(self):
        cases = [((5, 2), 3), ((2, 5), -3), ((0, 7), -7)]
        for (a, b), expect in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(self.calc.sub(a, b), expect)

    def test_mul(self):
        cases = [((-2, -3), 6), ((0.48, 0.43), 0.2064), ((0, 999), 0)]
        for (a, b), expect in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(self.calc.mul(a, b), expect)

    def test_div(self):
        cases = [((5, 2), 2.5), ((8, 7), 1.1428571428571428), ((-9, 3), -3.0)]
        for (a, b), expect in cases:
            with self.subTest(a=a, b=b):
                self.assertAlmostEqual(self.calc.div(a, b), expect, places=12)

        with self.assertRaisesRegex(ZeroDivisionError, "division by zero"):
            self.calc.div(114514, 0)

if __name__ == "__main__":
    unittest.main()
