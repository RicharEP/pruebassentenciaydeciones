import unittest
from evaluar_numero import evaluar_numero

class TestEvaluarNumero(unittest.TestCase):

    def test_positivo(self):
        self.assertEqual(evaluar_numero(5), "positivo")

    def test_negativo(self):
        self.assertEqual(evaluar_numero(-3), "negativo")

    def test_cero(self):
        self.assertEqual(evaluar_numero(0), "cero")

if __name__ == '__main__':
    unittest.main()
