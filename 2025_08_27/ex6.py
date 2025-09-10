'''Faça um programa que preencha um vetor com os modelos de cinco carros (exemplos de modelos: Fusca, Gol, Vectra, etc). 
Carregue outro vetor com o consumo desses carros, isto é, quantos quilômetros cada um deles faz com um litro de combustível.
Calcule e mostre:
O modelo do carro mais econômico; e 
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 Km.
'''
modelo = ['Fusca', 'Gol','Vectra', 'Palio', 'HB20']
consumo = [8, 9.5, 10, 12, 11.5]
menor_consumo = 0
posicao_menor = 0
distancia = 1000

for i in range(0,5): # identifica o mais economico
    if(consumo[i] < menor_consumo):
        posicao_menor = i

print(f"O modelo mais economico é: {modelo[posicao_menor]}")

for i in range(0,5):
    print(f"Para percorrer 1000 km o modelo: {modelo[i]}, consumirá: {(distancia/consumo[i]):.2f} litros")