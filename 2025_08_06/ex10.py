"""
Simulador de Caixa Eletrônico. 
Leia um valor para saque (múltiplo de 10) e exiba quantas notas de 100, 50, 20, 10 são necessárias.
Exemplo: R$ 80 → 1x R$50 + 1x R$20 + 1x R$10.
"""

saque = int(input("Informe o valor a sacar (múltiplo de 10): "))

sobra = saque
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0

notas100 = sobra//100
sobra = sobra - 100*notas100

notas50 = sobra//50
sobra = sobra - 50*notas50

notas20 = sobra//20
sobra = sobra - 20*notas20

notas10 = sobra//10
sobra = sobra - 10*notas10

print(f"Notas de 100: {notas100}")
print(f"Notas de 50: {notas50}")
print(f"Notas de 20: {notas20}")
print(f"Notas de 10: {notas10}")

