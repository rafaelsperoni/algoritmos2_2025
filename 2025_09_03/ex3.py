"""
Faça um algoritmo que lê estrutura (lista, tupla ou conjunto),
K que comporte 20 elementos. 
Troque a seguir os elementos de índice ímpar com 
os de índice par imediatamente seguinte mostre no final como ficou a estrutura K, com as alterações.
"""
k = []

for i in range(20):
    k.append(int(input(f"Informe valor para k[{i}]: ")))
    
#percorrer e trocar
for i in range(0,19,2):
    aux = k[i]
    k[i] = k[i+1]
    k[i+1] = aux

print(k)