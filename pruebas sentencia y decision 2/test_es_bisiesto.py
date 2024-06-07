import unittest
from es_bisiesto import es_bisiesto

class TestEsBisiesto(unittest.TestCase):

    def test_bisiesto_divisible_400(self):
        self.assertTrue(es_bisiesto(2000))
   
    def test_bisiesto_divisible_4_no_100(self):
        self.assertTrue(es_bisiesto(2024))
   
    def test_no_bisiesto_divisible_100_no_400(self):
        self.assertFalse(es_bisiesto(1900))
   
    def test_no_bisiesto_no_divisible_4(self):
        self.assertFalse(es_bisiesto(2019))

if __name__ == '__main__':
    unittest.main()
