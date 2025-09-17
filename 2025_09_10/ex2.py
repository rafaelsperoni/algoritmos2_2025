# M = [[0,0,0,0,0],
#      [0,0,0,0,0],
#      [0,0,0,0,0],
#      [0,0,0,0,0],
#      [0,0,0,0,0]]
# N = 5

# for c in range(N):
#     for l in range(N):
#         M[l][c] = int(input("valor: "))

M = []
N = 5

for i in range(5):
    linha = []
    M.append(linha)

for c in range(5):
    for l in range(5):
        print(f"linha {l} - coluna {c}")
        linha = M[l]
        linha.append(l)

