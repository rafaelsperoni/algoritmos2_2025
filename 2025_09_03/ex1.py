"""
Ler 2 duas estruturas (lista, tupla ou conjunto), denominada 
R de 5 elementos e S de 10 elementos, ambos de inteiros.
Gere outra estrutura X que possua os elementos comuns a R e a S.
Considere que na mesma estrutura não haverá números repetidos. 
"""

r = set()
s = set()

for i in range(5):
    r.add(int(input(f"Informe valor para r: ")))

for i in range(10):
    s.add(int(input(f"Informe valor para s: ")))
    
x = r & s

print(f"r {r}")
print(f"s {s}")
print(f"x {x}")