arquivo = open('aula.txt', 'w')  #abre para escrita

for linha in range(1,101):    # for de 1 a 100
   arquivo.write(f"Linha {linha} de 100\n")     #escreve texto no arquivo
   
arquivo.close()    #fecha o arquivo, salvando