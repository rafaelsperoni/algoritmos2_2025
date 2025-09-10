'''Faça um programa que preencha um vetor com 9 
números inteiros, calcule e mostre os que 
são números 
primos e suas respectivas posições.'''

l = []
cont = 0
for x in range(0,9):
    l.append(int(input(f"Informe um valor para a posição {x}: ")))

# l = [1,2,3,4,5,6,7,8,9]

for i in range(0,9): # acessa os elementos da lista
    for c in range(1,l[i]): # percorre os anteriores ao valor de i
        if (l[i] % c == 0):
            cont = cont + 1
    if(cont == 1):
        print(f"O valor de {l[i]} é primo e está na posição {i}")
    if(cont != 1):
        print(f"O valor de {l[i]} não é primo")
    cont = 0
