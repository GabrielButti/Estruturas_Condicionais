"""
40) O custo ao consumidor de um carro novo é a soma do custo de fábrica, da
comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados
sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e
escreva o custo ao consumidor
    |      CUSTO DE FÁBRICA          | % DO DISTRIBUIDOR | % DOS IMPOSTOS |
    | até R$12.000,00                |         5         |    isento      |
    | entre R$12.000,00 e 25.000,00  |        10         |      15        |
    | acima de R$25.000,00           |        15         |      20        |
"""

custoFabrica = float(input("Digite o custo de fábrica do carro: "))

custoConsumidor = 0.0

print()
if (custoFabrica > 0) and (custoFabrica <= 12000):
    custoConsumidor = custoFabrica + (custoFabrica * 0.05)
    print("5% da comissão do distribuidor")

elif (custoFabrica > 12000) and (custoFabrica <= 25000):
    custoConsumidor = custoFabrica + (custoFabrica * 0.1)
    print("10% da comissão do distribuidor")

elif custoFabrica > 25000:
    custoConsumidor = custoFabrica + (custoFabrica * 0.15)
    print("15% da comissão do distribuidor")

else:
    print("Valor inválido")


if (custoFabrica > 0) and (custoFabrica <= 12000):
    print("Isento de impostos")

elif (custoFabrica > 12000) and (custoFabrica <= 25000):
    custoConsumidor += custoFabrica * 0.15
    print("15% de impostos sobre o valor de fábrica")

elif custoFabrica > 25000:
    custoConsumidor += custoFabrica * 0.2
    print("20% de impostos sobre o valor de fábrica")


print("Valor do carro para o consumidor: %.2f" % custoConsumidor)