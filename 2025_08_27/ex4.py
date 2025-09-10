'''Ler um vetor R de 5 elementos, inteiros,
contendo o resultado da LOTO.
A seguir ler um vetor A de 10 elementos inteiros 
contendo uma aposta. 
A seguir imprima quantos pontos fez o apostador.
'''
r = []
a = []
cont = 0

for i in range(0,5):
    r.append(int(input(f"Informe um valor para a posição r[{i}]: ")))

for i in range(0,10):
    a.append(int(input(f"Informe um valor para a posição a[{i}]: ")))

for i in range(0,5): # percorre r
    for j in range(0, 10): # percorre s
        if (r[i] == a[j]): # compara se o valor existe na outra estrutura
            cont = cont + 1

print(f"O total de acerto foi de: {cont} ponto(s)")