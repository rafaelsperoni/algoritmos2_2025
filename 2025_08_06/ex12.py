"""
Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas. 
Exemplo: Nome = RAFAEL

"""

nome = input("Informe o nome: ")

for i in range(len(nome)):
    print(nome[0:i+1])