#Fazer umn programa que leia as listas codigo, nome e telefone, permitir uma consulta
codigo = []
cod = []
nome = []
telefone = []
cont = 2
for a in range(cont):
    codigo.append(input('digite um código de verificação: '))
    nome.append(input('digite seu nome, consagrado: '))
    telefone.append(int(input('digite seu telefone: ')))
acao = input('deseja realizar uma consulta? aperte 1 ou s: ')
if acao == 1 or acao == 's' or acao == 'S':
    for a in range(cont):
        cod.append = input('digite um código: ')
        if cod in codigo[a]:
            print('{}, {} possui o número 9{} '.format(codigo[a], nome[a], telefone[a]))
