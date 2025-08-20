"""
Faça um algoritmo que lê 10 valores para uma variável
do tipo lista de nome x. 
Após completar toda a leitura da lista,
verificar se cada valor armazenado na lista é par ou ímpar.
Se for par, fazer com que o valor seja atualizado
para o resultado da multiplicação do valor contido pelo índice. 
Se for impar fazer com que a lista receba o valor do
seu próprio índice.
"""
#cria lista vazia
L = []
#preenche a lista - leitura
for i in range(10):
    L.append(int(input(f"valor para posição {i}")))
    
#percorre a lista, testando e alterando
for i in range(10):
    if L[i]%2==0: #par
        L[i] = L[i] * i
    else:
        L[i] = i
        
print(L)