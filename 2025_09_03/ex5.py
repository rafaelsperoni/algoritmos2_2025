"""
Faça um programa que preencha duas estruturas (lista, tupla ou conjunto),
X e Y, com dez números inteiros cada.
Calcule e mostre o seguinte resultado:
A diferença entre X e Y:
"""
x = set()
y = set()

for i in range(10):
    x.add(int(input(f"Informe valor para r: ")))

for i in range(10):
    y.add(int(input(f"Informe valor para s: ")))
    
z = x - y

print(f"x {x}")
print(f"y {y}")
print(f"z {z}")