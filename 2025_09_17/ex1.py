M1 = []
M2 = []
R = []

N = int(input("Informe tamanho N, para uma matriz NxN: "))

print("Preenchimento de valores para a primeira matriz!")
for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Informe valor para M1[{l}][{c}]: "))
        linha.append(valor)
    M1.append(linha)

    
print("Preenchimento de valores para a segunda matriz!")
for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Informe valor para M2[{l}][{c}]: "))
        linha.append(valor)
        
    M2.append(linha)
    
for l in range(N):
    linha = []
    for c in range(N):
        linha.append( M1[l][c]+M2[l][c])
    R.append(linha)
    
print(M1)
print(M2)
print(R)