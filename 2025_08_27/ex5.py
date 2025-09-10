'''Faça um programa que preencha dois vetores de dez 
elementos numéricos cada um e mostre o vetor
resultante da intercalação deles:
'''
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 0]
a = []
b = []
c = [] # resultado

for i in range(0,10): # preenche A
    a.append(int(input(f"Informe um valor para a posição A[{i}]: ")))

for i in range(0,10): # preenche B
    b.append(int(input(f"Informe um valor para a posição b[{i}]: ")))

for i in range(0,10): # adiciona dois elementos por vez no vetor resultado um de A e outro de B
    c.append(a[i])
    c.append(b[i])

# mostra o resultado
print(c)