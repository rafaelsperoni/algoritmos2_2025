M = []
N = 2


for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Informe valor para M[{l}][{c}]: "))
        linha.append(valor)
    M.append(linha)
    
diag_principal = M[0][0] * M[1][1]
diag_secundaria = M[0][1] * M[1][0]
determinante = diag_principal - diag_secundaria

print(determinante)