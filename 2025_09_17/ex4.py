N = 5
M = []
SC = []
SL = []

print("Preenchimento de valores para a primeira matriz!")

for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Informe valor para M[{l}][{c}]: "))
        linha.append(valor)
    M.append(linha)
    
#soma das linhas
for l in range(N):
    somalinha = 0
    for c in range(N):
        somalinha += M[l][c]
    SL.append(somalinha)

#soma das colunas
for l in range(N):
    somacoluna = 0
    for c in range(N):
        somacoluna += M[c][l]
    SC.append(somacoluna)
    
print(M)
print(SL)
print(SC)