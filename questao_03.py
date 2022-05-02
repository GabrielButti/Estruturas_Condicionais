"""
3) Leia um número real. Se o número for positivo imprima a raiz quadrada.
Do contrário, imprima o número ao quadrado.
"""

num = float(input("Digite um número: "))

if num > 0:
    print("A raiz quadrada é:", (num ** 0.5))
else:
    print("Número ao quadrado:", (num ** 2))