"""
Leia uma palavra e conte quantas vogais (a, e, i, o, u) ela possui (use um laço de repetição e condicionais).
"""

palavra = input("Informe a palavra: ")

cont = 0
for c in palavra:
    if c.lower() in "aeiou" :
        cont+=1

print(f"Quantidade de vogais: {cont}")