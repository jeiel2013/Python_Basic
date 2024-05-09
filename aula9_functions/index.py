def ola_mundo():
    'Funções que mostra uma mensagem padrão na tela.'
    print('Olá Mundo!')
help(ola_mundo)
ola_mundo()

def olaMundo(name): #(name="User") será usado User como default
    'Função que mostra um texto customizado na tela.'
    print(f'Olá Mundo, meu nome é {name}')
nome = input('Qual o seu nome? ')
olaMundo(nome)

def soma(a,b):
    'Função que recebe dois números e realiza a soma entre eles'
    return a + b
resultado = soma(3,4)
