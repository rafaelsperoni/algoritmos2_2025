'''Faça um programa que preencha dois vetores, X e Y, 
com dez números inteiros cada. 
Calcule e mostre os seguintes vetores resultantes:
A diferença entre X e Y
'''
x = []
y = []
dif = []
cont = 0
for i in range(0,10):
    x.append(int(input(f"Informe um valor para a posição {i}: ")))

for i in range(0,10):
    y.append(int(input(f"Informe um valor para a posição {i}: ")))

x.sort()

x = [3,8,4,2,1,6,8,7,11,9]
y = [2,1,5,12,3,0,1,4,5,6]

for i in range(0,10): # indice de x
    for j in range(0,10): # indice de y
        if(x[i] == y[j]):
            break
        if(x[i] != y[j]):
            cont = cont + 1
    if(cont == 10) and (x[i] not in dif):
        dif.append(x[i])
    cont = 0

print(x)
print(y)
print(dif)