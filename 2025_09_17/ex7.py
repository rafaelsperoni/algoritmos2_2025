jogos = [
    ['Brasil', 'Italia', [10, 9]],
    ['Brasil', 'Espanha', [5, 7]],
    ['Italia', 'Espanha', [7,8]]
    ]

total = 0
for jogo in jogos:
    primeiro = jogo[0]  #primeiro time
    segundo = jogo[1]   #segundo time
    faltas = jogo[2]  #lista das faltas
    total = faltas[0] + faltas[1]

print(f"O total de faltas: {total}")

times = {}  #dicionario vazio

for jogo in jogos:
    primeiro = jogo[0]  #primeiro time
    segundo = jogo[1]   #segundo time
    faltas = jogo[2]  #lista das faltas
    total = faltas[0] + faltas[1]

    # acrescenta valores ao dicionario
    if primeiro in times:   #se já tem essa chave, soma o valor ao existente
        times[primeiro] += faltas[0] 
    else: #se não tem essa chave, cria e adiciona o valor
        times[primeiro] = faltas[0]
        
    if segundo in times: 
        times[segundo] += faltas[1]
    else:
        times[segundo] = faltas[1]
    
print(times) #mostra o dicionario criado, onde chave é o time, e valor o seu total de faltas

#cria uma lista com as chaves do dicionario (times) e uma com os valores (faltas)
lista_times = list(times.keys())
lista_faltas = list(times.values())

print(lista_times)
print(lista_faltas)      

menor = min(lista_faltas) #menor valor da lista
posmenor = lista_faltas.index(menor) #posicao do menor

print(f"País com menos faltas: {lista_times[posmenor]}")