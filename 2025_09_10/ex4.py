#matriz a partir de lista vazia
M = []  
N = 5 #tamanho

for l in range(5):  #for das linhas
    linha = [] #cria 
    for c in range(5):  #for das colunas
        linha.append(int(input(f"Valor para M[{l}][{c}]: ")))
    M.append(linha)
    
#soma dos valores da linha 4
#soma dos valores de M[4]
soma = 0
for i in range(5):
    soma += M[4][i]

print(f"A soma dos valores da linha 4: {soma}")