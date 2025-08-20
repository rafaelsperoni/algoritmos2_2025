"""
Altere o algoritmo anterior para que ele realize o produto
da primeira lista, pelo inverso da segunda lista.
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
    C.append(A[i] * B[4-i])
    
print(f"lista A: {A}")
print(f"lista B: {B}")
print(f"lista C: {C}")