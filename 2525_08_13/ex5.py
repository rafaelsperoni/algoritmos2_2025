"""
Faça um algoritmo que lê 10 valores para uma variável 
do tipo vetor e mostre qual a posição está armazenado 
o maior e o menor valor no vetor.
"""
import numpy as np

N = 5
x = np.zeros(N, dtype=int) #array de inteiros
#leitura dos valores e armazenamento no array
for i in range(N):
    x[i] = int(input(f"Informe o numero para a posição {i}: "))
    
#inicia com o primeiro
maior = menor = x[0]
posmaior = posmenor = 0
#percorre pra encontrar maior/menor
for i in range(1,N): #percorre a partir do segundo
    if x[i]>maior:
        maior = x[i]
        posmaior = i
    if x[i]<menor:
        menor = x[i]
        posmenor = i

print(f"O maior é {maior} e está na posição {posmaior}")
print(f"Conferindo com a função argmax() {x.argmax()}")
print(f"O menor é {menor} e está na posição {posmenor}")
print(f"Conferindo com a função argmin() {x.argmin()}")