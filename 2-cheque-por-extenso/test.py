from main import cheque
import unittest
from unittest import TestCase

class Test(TestCase):
    def teste_unidade(self):
        self.assertEqual(cheque(1), "um reais")
        self.assertEqual(cheque(9), "nove reais")

    def teste_dezena_dez(self):
        self.assertEqual(cheque(13), "treze reais")
        self.assertEqual(cheque(18), "dezoito reais")

    def teste_dezena(self):
        self.assertEqual(cheque(60), "sessenta reais")
    
    def teste_centena(self):
        self.assertEqual(cheque(100), "cem reais")
        self.assertEqual(cheque(153), "cento e cinquenta e tres reais")
        self.assertEqual(cheque(640), "seiscentos e quarenta reais")
        self.assertEqual(cheque(903), "novecentos e tres reais")
        self.assertEqual(cheque(300), "trezentos reais")

    def teste_unidade_de_milhar(self):
        self.assertEqual(cheque(1000), "mil reais")
        self.assertEqual(cheque(4000), "quatro mil reais")
        self.assertEqual(cheque(6300), "seis mil e trezentos reais")
        self.assertEqual(cheque(2940), "dois mil novecentos e quarenta reais")
        self.assertEqual(cheque(3615), "tres mil seiscentos e quinze reais")
        self.assertEqual(cheque(8765), "oito mil setecentos e sessenta e cinco reais")

if __name__ == '__main__':
    unittest.main()