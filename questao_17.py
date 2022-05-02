"""
17) Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
    A = ((basemaior + basemenor) * altura) / 2
Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""

baseMa = float(input("Digite a base maior do trapézio: "))
baseMe = float(input("Digite a base menos do trapézio: "))
alt = float(input("Digite a altura do trapézio: "))

if (baseMe > 0) and (baseMa > 0):
    Area = ((baseMa + baseMe) * alt) / 2
    print("A área do trapézio é: ", "%.2f" % Area)
else:
    print("Informe um valor válido.")