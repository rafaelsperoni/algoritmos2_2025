# # 1 - criando a matriz preenchida
# M = [[0,0,0,0,0],
#      [0,0,0,0,0],
#      [0,0,0,0,0],
#      [0,0,0,0,0],
#      [0,0,0,0,0]]
# N = 5

# for l in range(N):
#     for c in range(N):
#         M[l][c] = int(input(f"Valor para M[{l}][{c}]: "))
       
# for l in range(N):
#     for c in range(N):
#         print(M[l][c])
        
        
# 2 - Matriz como lista vazia
M = []  
N = 5

for l in range(5):
    linha = []
    for c in range(5):
        linha.append(int(input(f"Valor para M[{l}][{c}]: ")))
    M.append(linha)
      
for l in range(5):
    for c in range(5):
        print(M[l][c])