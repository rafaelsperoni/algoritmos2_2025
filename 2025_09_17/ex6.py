N = 5
L = []
M = []

print("Preenchimento da lista de 5 posições")
for i in range(5):
    L.append(int(input(f"Valor para L[{i}]")))

print("Preenchimento da matriz 5x5")
for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Informe valor para M[{l}][{c}]: "))
        linha.append(valor)
    M.append(linha)

print(f"Lista lida")
print(L)

print(f"Matriz lida")
print(M)    

#multiplicando item da lista por cada item da linha
for l in range(N):
    for c in range(N):
        M[l][c] = L[l] * M[l][c]
        
print(f"Matriz resultante")
print(M)