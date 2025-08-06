"""
Exiba os N primeiros termos da sequência de Fibonacci (ex: 0, 1, 1, 2, 3, 5... para N=5).
"""

n = int(input("Informe a quantidade: "))
anterior = 0
atual = 1
cont = 0

print(anterior)
print(atual)
while cont<n-2:
    proximo = anterior + atual
    print(proximo)
    anterior = atual
    atual = proximo
    
    cont+=1

