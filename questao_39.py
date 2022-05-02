"""
39) Uma empresa decide dar um aumento aos seus funcionários de acordo com uma
tabela que consideraa o salário atual e o tempo de serviço de cada funcionário.
Os funcionários com menor salário terão um aumento proporcionalmente maior do que
os funciopnários com um salário maior, e conforme o tempo de serviço na empresa, cada
funcionário irá receber um bônus adicional de salário. Faça um programa que leia:
    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na
    empresa).
Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima
o valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha
direito a nenhum aumento.
    |   Salário Atual   |   Reajuste    | Tempo de Serviço |  Bônus     |
    | Até 500,00        |     25%       | Abaixo de 1 ano  | Sem bônus  |
    | Até 1000,00       |     20%       | De 1 a 3 anos    |  100,00    |
    | Até 1500,00       |     15%       | De 4 a 6 anos    |  200,00    |
    | Até 2000,00       |     10%       | De 7 a 10 anos   |  300,00    |
    | Acima de 2000,00  | Sem reajuste  | Mais de 10 anos  |  500,00    |
"""

salarioAtual = float(input("Digite o salário do funcionário: "))
tempoServico = int(input("Digite o tempo de serviço do funcionário (Anos): "))

salarioFinal = 0.0

print()
if (salarioAtual > 0) and (salarioAtual <= 500):
    salarioFinal = salarioAtual + (salarioAtual * 0.25)

elif (salarioAtual > 500) and (salarioAtual <= 1000):
    salarioFinal = salarioAtual + (salarioAtual * 0.20)

elif (salarioAtual > 1000) and (salarioAtual <= 1500):
    salarioFinal = salarioAtual + (salarioAtual * 0.15)

elif (salarioAtual > 1500) and (salarioAtual <= 2000):
    salarioFinal = salarioAtual + (salarioAtual * 0.10)

elif salarioAtual > 2000:
    salarioFinal = salarioAtual

else:
    print("Salário inválido")


if (tempoServico >= 0) and (tempoServico < 1):
    print("Sem bônus")

elif (tempoServico >= 1) and (tempoServico <= 3):
    salarioFinal += 100
    print("Bônus de 100,00")
elif (tempoServico >= 4) and (tempoServico <= 6):
    salarioFinal += 200
    print("Bônus de 200,00")

elif (tempoServico >= 7) and (tempoServico <= 10):
    salarioFinal += 300
    print("Bônus de 300,00")

elif tempoServico > 10:
    salarioFinal += 500
    print("Bônus de 500,00")

else:
    print("Tempo de serviço inválido")


print("Salário final: %.2f" % salarioFinal)