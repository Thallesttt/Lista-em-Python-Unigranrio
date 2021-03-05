# exercício 4
nota = [] 
nome = []
notaturma = []
base=10
for i in range(base):
    nome.append(input('digite o nome do aluno: '))
    nota.append(float(input('digite um número: ')))
    notaturma.append( nota[i]+ base )
for i in range(base):
    if nota[i]> notaturma[i]:
        print('{},Parabéns. Sua nota é : {}'.format(nome[i], nota[i]))
