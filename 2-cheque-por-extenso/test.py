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
		self.assertEqual(cheque(37), "trinta e sete")
		
if __name__ == '__main__':
	unittest.main()