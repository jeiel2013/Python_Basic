# Exercício 1 - Fatorial
def ex1():
    num1 = eval(input('Digite um número: '))
    resultado = num1
    while num1 >= 2:
        resultado = resultado * (num1 - 1)
        num1 -= 1
        print(resultado)

# Exercício 2 - Tentativas de acertar senha
def ex2():
    senha = '1234'
    tentativas = 3
    while tentativas != 0:
        chance = input('Digite uma senha numerica de quatro digitos: ')
        if chance == senha:
            print('Senha correta. Acesso concedido')
            break
        else:
            print('Senha incorreta. Tente novamente.')
            tentativas -= 1

escolha = eval(input('Digite 1 para o exercício 1 ou 2 para exercício 2: '))
if escolha == 1:
    ex1()
elif escolha == 2:
    ex2()
else:
    print('NÃO HÁ MAIS EXERCICIOS!')
