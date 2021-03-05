# exercício 7
A = [] 
C = []
base=10
for i in range(base):
    A.append(int(input('digite um número: ')))
for i in range(base):
    C.append( A[i]**2)
    print(C[i])
