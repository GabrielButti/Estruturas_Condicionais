"""
6) Escreva um programa que, dados dois números inteiro, mostre na tela
o maior deles, assim como a diferença existente entre ambos.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))


if num1 > num2:
    print("O maior número é:", num1, "e a diferença existente é:", (num1 - num2))
else:
    print("O maior número é:", num2, "e a diferença existente é:", (num2 - num1))