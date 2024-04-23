import unittest

def fibonacci(valor):
    #condicion de corte
    if valor == 0:
        return 0
    if valor == 1:
        return 1
    #llamada recursiva
    return fibonacci(valor-1) + fibonacci(valor-2)

resultado = fibonacci(10)
print(resultado)


class TestFibonacci(unittest.TestCase):
    def test_9(self):
        resultado = fibonacci(9)
        self.assertEqual(resultado, 34)
 
    def test_10(self):
        resultado = fibonacci(10)
        self.assertEqual(resultado, 55)

    def test_11(self):
        resultado = fibonacci(11)
        self.assertEqual(resultado, 89)

if __name__ == '__main__':
    unittest.main()