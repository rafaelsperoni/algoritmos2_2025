""" 
Faça um algoritmo que lê 10 valores para uma variável 
do tipo lista de nome x e mostre os 10 valores armazenados.
"""

#resolução 2 - criando a lista vazia
L = []
for i in range(10):
    valor = int(input(f"Informe o valor para a posição {i}: "))
    L.append(valor)

#exibição da estrutura inteira
print(L)

#exibição item a item
for i in range(10):
    print(L[i])