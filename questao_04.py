"""
4) Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada ao número digitado
"""

num = int(input("Digite um número: "))

if num  > 0:
    print("O número ao quadrado é:", (num ** 2))
    print("A raiz do número é:", (num ** 0.5))
else:
    print("Número Inválido.")