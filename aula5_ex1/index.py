# Calcule a soma dos números do 10 ao 14
nums = [10, 11, 12, 13, 14]
print(sum(nums))
# Calcule a média entre os números 10,15,20
media = (10 + 15 + 20) / 3
print(media)
# Peça para o usuário digitar duas notas de zero a dez e os pesos das notas e calcule a média ponderada entre elas
# Exemplo: media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
# Lembrando que a soma dos pesos precisa ser dez
nota1 = int(input('Insira o valor da primeira nota (0 a 10): '))
# nota1 = eval(nota1)
nota2 = int(input('Insira o valor da segunda nota (0 a 10): '))
peso1 = int(input('Insira o valor do primeiro peso: '))
peso2 = int(input('Insira o valor do segundo peso: '))
medianotas = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
print(f'Media ponderada: {medianotas}')
# Qual o menor preço dessa lista? preços: R$100.20, R$34.90, R$31.50, R$18.95
lista = 100.20, 34.90, 31.50, 18.95
print(min(lista))
# Avalie se o número digitado pelo usuário é par ou ímpar. Se for par a saída deve mostrar True, se ímpar deverá mostrar False
n1 = int(input('Digite um número: '))
if n1 % 2 == 0:
    print('True')
else:
    print('False')
# Verifique se o menor preço dessa lista é menor que R$20,00; preços: R$100.20, R$34.90, R$31.50, R$18.95
if 20 < min(lista):
    print('True')
else:
    print('False')
# Faça um programa que converta a temperatura em graus Fahrenheit fornecida pelo usuário em graus celsius
num1 = int(input('Digite a temperatura em Fahrenheit: '))
celsius = (5/9) * (num1 - 32)
print(f"{celsius}° Celsius")