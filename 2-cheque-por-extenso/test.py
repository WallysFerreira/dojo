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

    def teste_unidade_de_milhar(self):
        self.assertEqual(cheque(1396), "mil trezentos e noventa e seis reais")
        self.assertEqual(cheque(4088), "quatro mil e oitenta e oito reais")
        self.assertEqual(cheque(7101), "sete mil cento e um reais")
        self.assertEqual(cheque(2220), "dois mil duzentos e vinte reais")


if __name__ == '__main__':
    unittest.main()