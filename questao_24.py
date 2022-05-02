"""
24) Uma empresa vende o mesmo produto para quatro diferentes estados.
Cada estado possui uma taxa diferente de imposto sobre o produto (MG 7%;
SP 12%; RJ %15; MS 8%). Faça um programa em que o usuário entre com o valor
e o estado destino do produto e o programa retorne o preço final do produto
acrescido do imposto do estado em que ele será vendido. Se o estado digitado
não for válido, mostrar uma mensagem de erro.
"""

valor = float(input("Digite o valor: "))
estado = input("Digite um Estado (MG), (SP), (RJ), (MS): ")

match estado:
    case "MG":
        valorFim = (valor + (valor * 0.07))
        print("Valor final acrescido com imposto é: " "%.2f" % valorFim)
    case "SP":
        valorFim = (valor + (valor * 0.12))
        print("Valor final acrescido com imposto é: " "%.2f" % valorFim)
    case "RJ":
        valorFim = (valor + (valor * 0.15))
        print("Valor final acrescido com imposto é: " "%.2f" % valorFim)
    case "MS":
        valorFim = (valor + (valor * 0.08))
        print("Valor final acrescido com imposto é: " "%.2f" % valorFim)
    case _:
        print("Estado Inválido.")