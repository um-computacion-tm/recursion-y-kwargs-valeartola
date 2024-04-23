import unittest

def fibonacci(valor):
    resultado = 1 
    while valor > 1: 
        resultado *= valor
        valor -= 1
    return resultado

class TestFibonacci(unittest.TestCase):
    def test_3(self):
        resultado = fibonacci(3)
        self.assertEqual(resultado, 6)
 
    def test_7(self):
        resultado = fibonacci(7)
        self.assertEqual(resultado, 5040)

    def test_11(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 3628800)

if __name__ == '__main__':
    unittest.main()