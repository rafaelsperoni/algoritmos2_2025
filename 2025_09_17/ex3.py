N = 4
M = []
print("Preenchimento de valores para a primeira matriz!")
for l in range(N):
    linha = []
    for c in range(N):
        valor = int(input(f"Informe valor para M[{l}][{c}]: "))
        linha.append(valor)
    M.append(linha)
    
a = int(input("Informe valor para a: "))

lista = []

for l in range(N):
    for c in range(N):
        lista.append(a * M[l][c])
        
print(lista)