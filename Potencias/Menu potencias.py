# Vamos fazer um programa que leia um número e faça a exponenciação e a radiciação de um número
def potencia(num1):
    return num1 ** 2


def raiz(num1):
    return num1**(1/2)


Menu = int(input('digite "1" para fazer o quadrado deste número ou "2" para fazer a raiz quadrada deste número'))
if Menu == 1:
    numero = int(input('Digite o numero que será usado: '))
    print(potencia(numero))
elif Menu == 2:
    numero = int(input('Digite o numero que será usado: '))
    print(raiz(numero))
else:
    print('ERRO')
