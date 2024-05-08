def ex1():
    nota1 = eval(input('Digite a primeira nota: '))
    nota2 = eval(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    if media >= 7:
        print(f'Sua media foi {media}. Você está aprovado. Parabens!')
    elif media >= 5:
        print('Voce esta de exame.')
    else: 
        print(f'Sua media foi {media}. Voce esta reprovado!')

ex1()