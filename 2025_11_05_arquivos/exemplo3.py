arq = open('sales.csv', 'r')

linhas = arq.readlines()

for l in linhas:
    colunas = l.split(',') # "quebra" um string
    print(f"Em {colunas[1]}, {colunas[2]} fez uma venda de {colunas[0]} ")