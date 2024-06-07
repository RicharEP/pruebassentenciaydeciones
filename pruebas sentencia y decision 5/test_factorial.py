import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def test_factorial_de_0(self):
        self.assertEqual(factorial(0), 1)
   
    def test_factorial_de_1(self):
        self.assertEqual(factorial(1), 1)
   
    def test_factorial_de_5(self):
        self.assertEqual(factorial(5), 120)
   
    def test_factorial_de_numero_grande(self):
        self.assertEqual(factorial(10), 3628800)
   
    def test_factorial_de_numero_negativo(self):
        with self.assertRaises(ValueError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()
