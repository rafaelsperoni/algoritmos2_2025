with open ("impares.txt", "w") as impares:
    with open ("pares.txt", "w") as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                impares.write(f"{n}\n")
        pares.close()
    impares.close()

with open('pares.txt', 'r') as pares:
    with open('impares.txt', 'r') as impares:
        with open('todos.txt', 'w') as todos:
            linhaspares = pares.readlines()
            linhasimpares = impares.readlines()
            for i in range(500):
                todos.write(linhaspares[i])
                todos.write(linhasimpares[i])
        todos.close()
    impares.close()
pares.close()