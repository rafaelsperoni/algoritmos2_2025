"""
Ler uma estrutura (lista, tupla ou conjunto), 
R de 5 elementos, inteiros, contendo o resultado da LOTO.
A seguir ler outra estrutura (lista, tupla ou conjunto),
A de 10 elementos inteiros contendo uma aposta.
A seguir imprima quantos pontos fez o apostador.
"""

r = set()
a = set()

for i in range(5):
    r.add(int(input(f"Informe valor para r: ")))

for i in range(10):
    a.add(int(input(f"Informe valor para s: ")))
    
x = r & a

print(f"r {r}")
print(f"a {a}")
print(f"x {a}")
print(f"Acertos: {len(x)}")