"""
20) Dados três valores A, B, C, verificar se eles podem ser valores
dos lados de um triângulo e, se forem, se é um triângulo escaleno,
equilátero ou isóscele, considerando os seguintes conceitos:
    - O comprimento de cada lado de um triângulo é menor
    do que a soma dos outros dois lados.
    - Chama-se equilátero o triângulo que tem três lados iguais
    - Denominam-se isósceles o triângulo que tem o comprimento
    de dois lados iguais.
    - Recebe o nome de escaleno o triângulo que tem os três lados diferentes.
"""

A = float(input("Digite o primeiro valor: "))
B = float(input("Digite o segundo valor: "))
C = float(input("Digite o terceiro valor: "))

if (A < (B + C)) and (B < (A + C)) and (C < ( A + B)):
    if (A == B) and (A == C):
        print("Triângulo Equilátero.")
    elif (A == B) or (A == C) or (B == C):
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Não é um triângulo")