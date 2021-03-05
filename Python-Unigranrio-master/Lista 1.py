# Lista para montar uma lista com 50 pessoas e botar as pessoas mais altas que 1.70
nome = []
altura = []
for i in range(3):
    nome.append(input('digite seu nome, consagrado: '))
    altura.append(float(input('Digite sua altura, consagrado: ')))
for i in range(3):
    if altura[i] > 1.70:
        print('{},meu consagrado, você é um dos maiores, e possui {} metros de altura'.format(nome[i], altura[i]))
