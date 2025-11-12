arquivo = open('aula.txt', 'r') #abre em modo leitura

linhas = arquivo.readlines()   #transforma em uma lista das linhas

for linha in linhas:  #percorre a lista
    print(linha)      #exibe item da lista
    
arquivo.close()