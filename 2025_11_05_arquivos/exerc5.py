#apenas criando outro, para manter o pares.txt original
with open ("pares2.txt", "w") as pares:
    for n in range(0, 1000):
        if n % 2 == 0:
            pares.write(f"{n}\n")
    pares.close()

with open('pares2.txt', 'r') as pares:            
    linhas = pares.readlines()
    pares.close()


with open('pares2.txt', 'w') as pares:
    for i in range(len(linhas)-1, -1, -1):
        pares.write(linhas[i])
    
    pares.close()