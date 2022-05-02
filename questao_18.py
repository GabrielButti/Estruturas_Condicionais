"""
18) Faça um programa que mostre ao usuário um menu com 4 opções de operações
matemáticas(as básicas, por exemplo). O usuário escolhe uma das opções e o seu
programa então pede dois valores numéricos e realiza a operação, mostrando o
resultado e saindo.
"""

opera = input("Escolha uma operação (+), (-), (*), (/): ")


match opera:
    case "+":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A soma dos valores é: ", "%.2f" % (num1 + num2))
    case "-":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A subtração dos valores é: ", "%.2f" % (num1 - num2))
    case "*":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A multiplicação dos valores é: ", "%.2f" % (num1 * num2))
    case "/":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A divisão dos valores é: ", "%.2f" % (num1 / num2))
    case _:
        print("Valor Inválido.")