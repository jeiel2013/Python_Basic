import random

numeroMinimo = int(input('Qual o numero minimo do intervalo?\n'))
numeroMaximo = int(input('Qual o numero maximo do intervalo?\n'))

tentativas = int(input('Quantas tentativas para acertar?\n'))

numeroSorteado = random.randint(numeroMinimo, numeroMaximo)

while True:
    tentativa = int(input(f'Digite um numero entre {numeroMinimo} e {numeroMaximo}.\n'))
    
    if tentativa == numeroSorteado:
        print('Parabéns! Você acertou o número.')
        break
    else:
        tentativas -= 1
        if tentativas == 0:
            print(f'Você não acertou o número e não tem mais tentativas. O número era {numeroSorteado}.')
            break
        else:
            print(f'Número errado. Tente novamente. Você ainda tem {tentativas} tentativas.')