"""
Escreva um programa que receba do usuário 5
números inteiros e o nome do arquivo no
qual eles devem ser armazenados.
Em seguida, ler do arquivo os valores armazenados
copiando-os para uma lista de inteiros 
e os imprimindo na tela.
"""

with open('numeros.txt', 'w') as arq:
    for i in range(5):
        num = int(input("Informe numero: "))
        arq.write(f"{num}\n")
    arq.close()
    
numeros = []

with open('numeros.txt', 'r') as arq:
    linhas = arq.readlines()
    for linha in linhas:
        numeros.append(int(linha))
    arq.close()
    
print(numeros)
