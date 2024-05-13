import random

#cria uma lista de palavras que serão sorteadas.
palavras = ['python', 'programacao', 'computador', 'aula', 'variavel', 'computador']

# escolhemos as palavras
palavraSorteada = random.choice(palavras)

# Criamos uma string com traços que representam as letras
palavraEscondida = '*' * len(palavraSorteada)

# criamos uma lista vazia para armazenar as letras que já foram digitadas
letrasAdivinhadas = []
maxTentativas = len(palavraSorteada)

while True:
    # mostra na tela a palavra escondida
    print(palavraEscondida)

    # pedimos ao jogador para digitar uma letra
    letra = input('Digite uma letra: ')

    # verificamos se a letra já foi digitada
    if letra in letrasAdivinhadas:
        print('Você já digitou essa letra. Tente outra por favor.')
        continue

    # adicionar a letra a lista de letras digitadas
    letrasAdivinhadas.append(letra)

    # verificar se a letra digitada está na palavra sorteada
    if letra in palavraSorteada:
        lista = []
        for indice in range(len(palavraSorteada)):
            if letra == palavraSorteada[indice]:
                lista.append(letra)
            else: 
                lista.append(palavraEscondida[indice])
        palavraEscondida = ''.join(lista)
    else:
        maxTentativas -= 1
        print(f'Letra não encontrada. Você tem mais {maxTentativas} tentativas.')

    if palavraEscondida == palavraSorteada:
        print(f'Parabéns, Você ganhou!! A palavra era {palavraSorteada}.')
        break
    elif maxTentativas == 0:
        print(f'Você perdeu. A palavra era {palavraSorteada}.')
        break