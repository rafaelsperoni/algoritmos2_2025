#matriz a partir de lista vazia
M = []  
N = 10 #tamanho

for l in range(N):  #for das linhas
    linha = [] #cria 
    for c in range(N):  #for das colunas
        linha.append(int(input(f"Valor para M[{l}][{c}]: ")))
    M.append(linha)

#soma dos valores da coluna 2
soma = 0
for l in range(N):
    soma += M[l][2]

print(f"Soma dos valores da coluna 2: {soma}")

#soma dos valores da diagonal principal
soma = 0
for i in range(N):
    soma += M[i][i]

print(f"Soma dos valores da diagonal: {soma}") 