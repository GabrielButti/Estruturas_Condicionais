"""
2) Leia um número fornecido pelo usuário. Se esse número for positivo,
calcule a raiz quadrada do número. Se o número for negativo, mostre
uma mensagem dizendo que o número é inválido.
"""

num = int(input("Digite um número: "))

if num > 0:
    print("A raiz quadrada do número é:", (num ** 0.5))
else:
    print("Número inválido.")