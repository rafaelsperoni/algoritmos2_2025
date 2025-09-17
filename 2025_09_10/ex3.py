#matriz a partir de lista vazia
M = []  
N = 5 #tamanho

for l in range(5):  #for das linhas
    linha = [] #cria 
    for c in range(5):  #for das colunas
        linha.append(int(input(f"Valor para M[{l}][{c}]: ")))
    M.append(linha)
    
#diagonal principal - [0][0]  [1][1]  [2][2] [3][3] [4][4]  
#ou seja, linha=coluna

for l in range(5):
    for c in range(5):
        if l==c:
            print(M[l][c])
            
#ou, fazendo apenas com um for
for i in range(5):
    print(M[i][i])