nome = input("Informe o seu nome: ")

with open('nome.txt', 'w') as arq:
    arq.write(nome)
    arq.close()
