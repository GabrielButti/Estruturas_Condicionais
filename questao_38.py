"""
38) Leia uma data de nascimento de uma pessoa fornecida através de três números
inteiros: Dia, Mês e Ano. Teste a validade desta data para saber se esta é uma
data válida. Teste se o dia fornecido é um dia válido: dia > 0, dia <= 28 para o mês
(29 se o ano for bissexto), dia <= 30 em abril, junho, setembro e novembro,
dia <= 31 nos outros meses. Teste a validade do mês: mês > 0 e mês <13. Teste a
validade do ano: ano <= ano atual (use uma constante definida com o valor igual a 2008).
Imprimir: "data válida" ou "data inválida" no final da execução.
"""

ano = int(input("Digite o ano do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
dia = int(input("Digite o dia do seu nascimento: "))

anoAtual = 2008

print()
if ano <= anoAtual:
    if mes == 1:

        if (dia >= 1) and (dia <= 31):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 2:

        if (ano % 400 == 0) or ((ano % 4 == 0) and not (ano % 100 == 0)):
            if (dia >= 1) and (dia <= 29):
                print("Data Válida")
            else:
                print("Data Inválida")

        else:
            if (dia >= 1) and (dia <= 28):
                print("Data Válida")
            else:
                print("Data Inválida")

    elif mes == 3:
        if (dia >= 1) and (dia <= 31):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 4:
        if (dia >= 1) and (dia <= 30):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 5:
        if (dia >= 1) and (dia <= 31):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 6:
        if (dia >= 1) and (dia <= 30):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 7:
        if (dia >= 1) and (dia <= 31):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 8:
        if (dia >= 1) and (dia <= 31):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 9:
        if (dia >= 1) and (dia <= 30):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 10:
        if (dia >= 1) and (dia <= 31):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 11:
        if (dia >= 1) and (dia <= 30):
            print("Data Válida")

        else:
            print("Data Inválida")

    elif mes == 12:
        if (dia >= 1) and (dia <= 31):
            print("Data Válida")

        else:
            print("Data Inválida")

    else:
        print("Data Inválida")

else:
    print("Data Inválida")