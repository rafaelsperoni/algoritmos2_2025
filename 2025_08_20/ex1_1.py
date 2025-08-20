""" 
Faça um algoritmo que lê 10 valores para uma variável 
do tipo lista de nome x e mostre os 10 valores armazenados.
"""

#resolução 1 - criando a lista com 10 posições zeradas
L = [0,0,0,0,0,0,0,0,0,0]
for i in range(10):
    valor = int(input(f"Informe o valor para a posição {i}: "))
    L[i] = valor

#exibição da estrutura inteira
print(L)

#exibição item a item
for i in range(10):
    print(L[i])