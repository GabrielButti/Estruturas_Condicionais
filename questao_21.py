"""
21) Escreva o menu de opções abaixo. Leia a opção do usuário e
execute a operação escolhida. Escreva uma mensagem de erro se a opção for inválida.
    Escolha a opção:
    1 - Soma de 2 números.
    2 - Diferença entre 2 número (maior pelo menor).
    3 - Produto entre 2 números.
    4 - Divisão entre 2 números (o denominador não pode ser zero).
    Opção
"""

print("(+) - Soma de 2 números."
      "\n(-) - Diferença entre 2 número (maior pelo menor)."
      "\n(*) - Produto entre 2 números."
      "\n(/) - Divisão entre 2 números (o denominador não pode ser zero).")

opera = input("Escolha uma opção: ")

match opera:
    case "+":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A soma dos valores é: ", "%.2f" % (num1 + num2))
    case "-":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if (num1 < num2):
            print("Não é possível subtrair.")
        else:
            print("A subtração dos valores é: ", "%.2f" % (num1 - num2))
    case "*":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print("A multiplicação dos valores é: ", "%.2f" % (num1 * num2))
    case "/":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if (num2 == 0):
            print("Não é possível dividir.")
        else:
            print("A divisão dos valores é: ", "%.2f" % (num1 / num2))
    case _:
        print("Valor Inválido.")