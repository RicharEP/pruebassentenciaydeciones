import unittest
from es_palindromo import es_palindromo

class TestEsPalindromo(unittest.TestCase):

    def test_palindromo_simple(self):
        self.assertTrue(es_palindromo("reconocer"))
   
    def test_palindromo_con_espacios(self):
        self.assertTrue(es_palindromo("anita lava la tina"))
   
    def test_palindromo_con_mayusculas(self):
        self.assertTrue(es_palindromo("A Santa at NASA"))
   
    def test_no_palindromo(self):
        self.assertFalse(es_palindromo("python"))
   
    def test_cadena_vacia(self):
        self.assertTrue(es_palindromo(""))

if __name__ == '__main__':
    unittest.main()
