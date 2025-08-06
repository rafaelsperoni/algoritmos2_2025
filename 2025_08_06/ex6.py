"""
Peça um número inteiro positivo N e calcule a soma de todos os números de 1 até N.
Exemplo: Se N = 5 → 1 + 2 + 3 + 4 + 5 = 15.
"""

n = int(input("Informe num: "))

soma = 0
for i in range(1, n+1):
    soma += i

print(soma)