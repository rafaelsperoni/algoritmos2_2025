nome = input("Informe o seu nome: ")
with open('nome.txt', 'w') as arq:
    arq.write(nome)
    arq.close()

with open('nome.txt', 'a') as arq:
    arq.write('Eu amo algoritmos')
    arq.close()
