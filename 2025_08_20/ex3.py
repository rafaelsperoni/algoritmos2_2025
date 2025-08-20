"""
Elabore um algoritmo que leia duas listas de 5 posições,
após a leitura, crie uma terceira lista contendo as somas
dos elementos das posições correspondentes das listas lidas.
Apresente as listas.
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
    
C = []
for i in range(N):
    C.append(A[i] + B[i])
    
print(f"lista A: {A}")
print(f"lista A: {B}")
print(f"lista A: {C}")