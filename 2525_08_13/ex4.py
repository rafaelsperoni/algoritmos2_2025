"""
Faça um algoritmo que lê 5 valores para uma variável 
do tipo vetor e determine o maior e o menor valor
armazenado no vetor.
"""

import numpy as np

N = 5
x = np.zeros(N, dtype=int) #array de inteiros
#leitura dos valores e armazenamento no array
for i in range(N):
    x[i] = int(input(f"Informe o numero para a posição {i}: "))
    
#inicia com o primeiro
maior = menor = x[0]

#percorre pra encontrar maior/menor
for i in range(1,N): #percorre a partir do segundo
    if x[i]>maior:
        maior = x[i]
    if x[i]<menor:
        menor = x[i]

print(f"O maior: {maior}")
print(f"Conferindo com a função max(): {x.max()}")

print(f"O menor: {menor}")
print(f"Conferindo com a função min(): {x.min()}")