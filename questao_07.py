"""
7) Faça um programa que receba dois números e mostre o maior.
Se por acaso, os dois números forem iguais, imprima a mensagem
'Números iguais'.
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O número maior é:", num1)
elif num2 > num1:
    print("O número maior é:", num2)
else:
    print("Números iguais")