# Segunda lista, onde deve-se criar uma lista para colocar 100 pessoas e calcular o salário e o desconto, além do salário liquido
mat = []
salbruto = []
saliq = []
des = []
a = 100
for i in range(a):
    mat.append(input('digite sua matrícula irmão: '))
    salbruto.append(float(input('Digite seu salário: ')))
for i in range(a):
    des.append((salbruto[i] / 100) * 11)
    saliq.append(salbruto[i] - des[i])
    print('O senhor/a, de matrícula {} possui o salário líquido {}'.format(mat[i], saliq[i]))
