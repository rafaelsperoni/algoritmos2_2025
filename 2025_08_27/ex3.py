'''Ler 2 vetores, 
R de 5 elementos e
S de 10 elementos, ambos de inteiros.
 Gere um vetor X que possua os elementos comuns a R e a S. 
 Considere que no mesmo vetor não haverá números repetidos. '''

r = [1, 2, 3, 4, 5]  #0..4
s = [2, 4, 6, 7, 1, 6, 7, 8, 9, 0] #0..9
x = []

##primeira forma
for valor in r: #percorre lista r
    print(valor)  # acessa o item da lista
    if valor in s:  #se o valor está contido na lista s
        x.append(valor)  #adiciona o valor na lista x

##segunda forma
# for i in range(5):
#     for j in range(10):
#         if r[i] == s[j]: #achei valor igual
#             #guardar em x
#             x.append(r[i])

print(x)
print(len(x))