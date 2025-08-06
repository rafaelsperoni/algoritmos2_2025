"""
Faça um programa que solicite valores inteiros fornecidos pelo usuário até ele informar o valor 0 (zero).
Em seguida, identifique e exiba quantos números ímpares e os pares foram fornecidos, sem considerar o valor 0.
"""

pares = 0
impares = 0

while True:
    num = int(input("Informe numero inteiro (0 para sair):"))
    if num==0:
        break
    
    if num%2 == 0:
        pares+=1
    else:
        impares +=1
           
print(f"Total de números lidos: {pares+impares}")
print(f"Quantidade de Pares: {pares}")
print(f"Quantidade de Impares: {impares}")