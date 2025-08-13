"""
Faça um algoritmo que lê 10 valores para uma variável do 
tipo vetor de nome x e mostra os 10 valores armazenados na estrutura.
"""
import numpy as np

N = 10

x = np.zeros(N, dtype=int) #array de inteiros

for i in range(N):
    x[i] = int(input(f"Informe o numero para a posição {i}: "))
    
#exibe o vetor inteiro
print(x)

#exibe cada posição do vetor
for i in range(N):
    print(x[i])