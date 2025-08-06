"""
Verifique se um número N é perfeito (igual à soma de seus divisores próprios, exceto ele mesmo).
Exemplo: 6 (1 + 2 + 3 = 6) → É perfeito.
"""

n = int(input("Informe o número: "))
soma = 0
for i in range(1, n):
    if n%i==0:
        soma += i

if soma==n:
    print(f"{n} é Perfeito")