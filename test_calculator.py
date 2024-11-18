import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add1(self):
        self.assertEqual(self.calc.add(-6, 4), -2)
    def test_add2(self):
        self.assertEqual(self.calc.add(-9, -7), -16)
    def test_sub1(self):
        self.assertEqual(self.calc.subtract(-4, -9), 5)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
    def test_mul1(self):
        self.assertEqual(self.calc.multiply(8, 4), 32)
    def test_mul2(self):
        self.assertEqual(self.calc.multiply(-6, 5), -30)
    def test_div1(self):
        self.assertEqual(self.calc.divide(60, 6), 10)
    def test_div2(self):
        self.assertEqual(self.calc.divide(-80, 0), 0)
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(38, 3), 2)
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(100, 25), 0)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()