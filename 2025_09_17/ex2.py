N = 10
M = []
print("Preenchimento de valores para a primeira matriz!")
for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Informe valor para M[{l}][{c}]: "))
        linha.append(valor)
    M.append(linha)

print("Matriz lida: ")
print(M)

#trocar valores da linha de indice 2 com a linha de indice 8
for c in range(N):
    aux = M[2][c]
    M[2][c] = M[8][c]
    M[8][c] = aux
    
#troca valores da linha de indice 5 com a coluna de indice 9
for c in range(N):
    aux = M[5][c]
    M[5][c] = M[c][9]
    M[c][9] = aux

print("Matriz resultante: ")
print(M)