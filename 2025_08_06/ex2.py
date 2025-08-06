"""
A prefeitura de uma cidade fez uma pesquisa com 100 pessoas, coletando dados sobre o salário e o	número de filhos. A prefeitura deseja	 saber:	 
A média do salário dessas pessoas
A média do número de filhos
O maior salário
A percentagem de pessoas com salários até R$ 1500,00
"""
quantidade = 5
somasal = 0.0
mediasal = 0.0
somafil = 0
mediafil = 0.0
maiorsal = 0.0
percent = 0.0
contamenores = 0
for i in range(quantidade):
    salario = float(input("Informe salário: "))
    filhos = int(input("Quantidade de filhos: "))
    
    if i==0 or salario>maiorsal:
        maiorsal = salario

    somasal += salario
    somafil += filhos
    
    if salario<1500.0:
        contamenores += 1
        
    
mediasal = somasal/quantidade
mediafil = somafil / quantidade
percent = contamenores / quantidade * 100
print(f"Maior salário: {maiorsal}")
print(f"Média dos salários: {mediasal}")
print(f"Média de filhos: {mediafil}")
print(f"Percentagem de pessoas com salario menor que R$1.500,00: {percent}%")