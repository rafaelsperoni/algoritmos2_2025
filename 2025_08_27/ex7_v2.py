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

for i in x:
    if(i not in y) and (i not in dif):
        dif.append(i)


print(x)
print(y)
print(dif)