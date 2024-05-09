# Exercício 1 - Calcular quadrado
def quadrado(n = 5):
    return n * n

# Exercício 2 - Fahrenheit para Celsius
def convert(f):
    celsius = (5/9) * (f - 32)
    return celsius

# Exercício 3 
def mat(q, c):
    if q == 'quadrado':
        return c * c
    else:
        return c * c * c
    