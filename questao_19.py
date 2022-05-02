"""
19) Faça um programa para verificar se um determinado número
inteiro é divisível por 3 ou 5, mas não simultaneamente pelos dois.
"""

num = int(input("Digite um número inteiro: "))

if (num % 3 == 0) and not (num % 5 == 0):
    print("Número divisível por 3")
elif (num % 5 == 0) and not (num % 3 == 0):
    print("Número divisível por 5")
else:
    print("Número Inválido.")