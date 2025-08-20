"""
Faça um algoritmo que lê duas listas A e B com 5 elementos cada.
Construir uma lista C, sendo este a junção das duas outras listas,
ou seja, a lista C deverá conter 10 elementos. Mostre no final a lista C.
"""
A = []
B = []

N = 5

print("Preenchendo a lista A: ")
for i in range(N):
    A.append(int(input(f"Informe valor para A[{i}]: ")))

print("Preenchendo a lista B: ")
for i in range(N):
    B.append(int(input(f"Informe valor para B[{i}]: ")))

#opcao 1 - operação de soma
C = A + B

#opcao 2 - item a item
D = []
for i in range(N):
    D.append(A[i])
for i in range(N):
    D.append(B[i])

    
print(f"lista A: {A}")
print(f"lista B: {B}")
print(f"lista C: {C}")
print(f"lista D: {D}")