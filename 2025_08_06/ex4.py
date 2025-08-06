"""
Exiba todos os números ímpares de 1 até um número N fornecido pelo usuário (use while ou for).
"""
n = int(input("Informe o numero: "))

for i in range(1,n+1):
    if i%2!=0:
        print(i)