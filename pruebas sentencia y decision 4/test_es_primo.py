import unittest
from es_primo import es_primo

class TestEsPrimo(unittest.TestCase):

    def test_primo_2(self):
        self.assertTrue(es_primo(2))
   
    def test_primo_3(self):
        self.assertTrue(es_primo(3))
   
    def test_primo_grande(self):
        self.assertTrue(es_primo(7919))  # 7919 es un número primo
   
    def test_no_primo_4(self):
        self.assertFalse(es_primo(4))
   
    def test_no_primo_10(self):
        self.assertFalse(es_primo(10))
   
    def test_no_primo_grande(self):
        self.assertFalse(es_primo(7907))  # 7907 no es un número primo

if __name__ == '__main__':
    unittest.main()
