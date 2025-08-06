"""
Faça um programa que leia o nome do usuário e mostre o nome de trás para frente, utilizando somente letras maiúsculas. 
NÃO UTILIZE FUNÇÃO PARA REVERTER!
"""

inverso = ""

nome = input("Informe o nome: ")

tam = len(nome)

for i in range(tam-1, -1, -1):
    inverso += nome[i]

print(inverso)