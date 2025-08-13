"""
Faça um algoritmo que lê 5 valores para uma variável do
tipo vetor e determine a média de todos os valores
armazenados no vetor.
"""
import numpy as np

N = 5
soma = 0

x = np.zeros(N, dtype=int) #array de inteiros
#leitura dos valores e armazenamento no array
for i in range(N):
    x[i] = int(input(f"Informe o numero para a posição {i}: "))
    
#percorre para fazer a soma
for i in range(N):
    soma += x[i]

media = soma/N    
print(f"A média dos valores armazenados: {media}")

print(f"Conferindo com a função mean(): {x.mean()}")

    