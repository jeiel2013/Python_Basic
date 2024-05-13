import math

def composto(capital, juros, tempo):
    return capital*math.pow((1 + juros), tempo)

def simples(capital, juros, tempo) :
    return capital*juros*tempo

capital = float(input('Qual o capital de investimento? '))
juros = float(input('Qual o juros anual em porcentagem (%)? '))
tempo = int(input('Quantos meses será o investimento? '))

juros = juros / 100 # 3% = 3 / 100
tempo = tempo / 12

valorFinalComposto = composto(capital, juros, tempo)
print(f'O montante final será de R${valorFinalComposto:.02f}')
print(f'Os Juros do rendimento foram de: {(valorFinalComposto - capital):.02f}')

valorFinalSimples = simples(capital, juros, tempo)
print(f'O montante final será de R${(valorFinalSimples + capital):.02f}')