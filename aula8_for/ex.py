# Exerício 1 - Tabuada
def ex1():
    tabuada = int(input('Qual a tabuada será gerada? '))
    limite = int(input('Até qual valor iremos calcular? '))
    for numero in range(0, limite + 1):
        print(f'{tabuada} x {numero} = {tabuada * numero}')

# Exercício 2 - Fibonacci
def ex2():
    n = int(input('Digite qual elemento da serie deve ser mostrado: '))
    primeiro = 1
    segundo = 1
    if n == 1 or n == 2:
        print('1')
    else:
        for _ in range(2, n):
            elemento = primeiro + segundo
            segundo = primeiro
            primeiro = elemento
        print(elemento)

escolha = eval(input('Digite 1 para o exercício 1 ou 2 para exercício 2: '))
if escolha == 1:
    ex1()
elif escolha == 2:
    ex2()
else:
    print('NÃO HÁ MAIS EXERCICIOS!')