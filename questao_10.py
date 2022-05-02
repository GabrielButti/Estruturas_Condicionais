"""
10) Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre
seu peso ideal, utilizando as sequintes fórmulas (onde h corresponde à altura):
    - Homens: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 58
"""

alt = float(input("Digite sua altura: "))
sexo = (input("Digite seu sexo (M/F): "))

print()

if sexo == "M":
    pesoIdeal = (72.7 * alt) - 58
    print("Seu peso ideal é:", "%.2f" % pesoIdeal)
else:
    PesoIdeal = (62.1 * alt) - 58
    print("Seu peso ideal é:", "%.2f" % pesoIdeal )