"""
Leia dois números A e B (A < B) e um número K.
Calcule a soma de todos os números entre A e B (inclusive) que são divisíveis por K.
Exemplo: A=10, B=20, K=3 → 12 + 15 + 18 = 45.
"""

a = int(input("Informe A: "))
b = int(input("Informe B: "))
k = int(input("Informe k: "))
soma = 0
for i in range(a, b+1):
    if i%k==0:
        soma += i

print(soma)