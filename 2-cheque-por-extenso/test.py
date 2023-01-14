from main import cheque
import unittest
from unittest import TestCase

class Test(TestCase):
    def teste_unidade(self):
        self.assertEqual(cheque(1), "um")
        self.assertEqual(cheque(9), "nove")

    def teste_dezena_dez(self):
        self.assertEqual(cheque(13), "treze")
        self.assertEqual(cheque(18), "dezoito")

    def teste_dezena(self):
        self.assertEqual(cheque(60), "sessenta")
    
    def teste_centena(self):
        self.assertEqual(cheque(100), "cem")
        self.assertEqual(cheque(153), "cento e cinquenta e tres")
        self.assertEqual(cheque(640), "seiscentos e quarenta")

if __name__ == '__main__':
    unittest.main()