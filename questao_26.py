"""
26) Leia a distância em km e a quantidade de litros de gasolina consumidos
por um carro em um percurso, calcule o consumo em km/l e escreva uma mensagem
de acordo com a tabela abaixo:
    CONSUMO     |  (Km/l)  |   MENSAGEM
    menor que   |     8    |  Venda o carro!
    entre       |  8 e 12  |     Econômico!
    maior que   |    12    |  Super econômico!
"""

distancia = float(input("Digite uma distância (Km): "))
litros = float(input("Digite a quantidade de litros consumidos: "))

consumo = distancia / litros

if consumo < 8:
    print("Venda o carro!")
elif (consumo >= 8) and (consumo <= 12):
    print("Econômico!")
else:
    print("Super Econômico!")