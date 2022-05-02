"""
28) Faça um programa que leia três números inteiros positivos e efetue
o cálculo de uma das seguintes médias de acordo com um valor numérico
digitado pelo usuário:
    (a) Geométrica: ³√x * y * z
    (b) Ponderada: (x + 2 * y + 3 * z) / 6
    (c) Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))
    (d) Aritmética: (x + y + z) / 3
"""

print("(1) Geométrica: ³√x * y * z"
      "\n(2) Ponderada: (x + 2 * y + 3 * z) / 6"
      "\n(3) Harmônica: 1 / ((1 / x) + (1 / y) + (1 / z))"
      "\n(4) Aritmética: (x + y + z) / 3")

opcao = int(input("Digite a opção de média desejada: "))

match opcao:
    case 1:
        X = int(input("Digite o primeiro número: "))
        Y = int(input("Digite o segundo número: "))
        Z = int(input("Digite o terceiro número: "))
        mediaG = ((X ** (1 / 3)) * Y * Z)
        print("A Média Geométrica é:", "%.2f" % mediaG)
    case 2:
        X = int(input("Digite o primeiro número: "))
        Y = int(input("Digite o segundo número: "))
        Z = int(input("Digite o terceiro número: "))
        mediaP = (((X + 2) * (Y + 3) * Z) / 6)
        print("A Média Ponderada é:", "%.2f" % mediaP)
    case 3:
        X = int(input("Digite o primeiro número: "))
        Y = int(input("Digite o segundo número: "))
        Z = int(input("Digite o terceiro número: "))
        mediaH = (1 / ((1 / X) + (1 / Y) + (1 / Z)))
        print("A Média Harmônica é:", "%.2f" % mediaH)
    case 4:
        X = int(input("Digite o primeiro número: "))
        Y = int(input("Digite o segundo número: "))
        Z = int(input("Digite o terceiro número: "))
        mediaA = ((X + Y + Z) / 3)
        print("A Média Aritmética é:", "%.2f" % mediaA)