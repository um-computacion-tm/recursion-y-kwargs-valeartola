import unittest

def factorial(valor):
    resultado = 1 
    while valor > 1: 
        resultado *= valor
        valor -= 1
    return resultado

class TestFactorial(unittest.TestCase):

    def test_1(self):
        self.assertEqual(factorial(1), 1)
    def test_5(self):
        self.assertEqual(factorial(5), 120)
    def test_10(self):
        self.assertEqual(factorial(10), 3628800)
    def test_8(self):
        self.assertEqual(factorial(8), 40320)


if __name__ == '__main__':
    unittest.main()
