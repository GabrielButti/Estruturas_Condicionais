"""
14) A nota final de um estudante é calculada a partir de três notas atribuídas entre
o intervalo de 0 até 10, respectivamente, a trabalho do laboratório, a uma avaliação
semestral e a um exame final. A média das três notas mencionada anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliaçõ Semestral: 3; Exame final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2.9),
de recuperação (entre 3 e 4.9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

trabLab = float(input("Digite a nota do Trabalho do Ladoratório: "))
avaSem = float(input("Digite a nota da Avaliação Semestral: "))
examFim = float(input("Digite a nota do Exame Final: "))

mediaPond = ((trabLab * 2) + (avaSem * 3) + (examFim * 5)) / 10

if (mediaPond >= 0) and (mediaPond <= 2.9):
    print("Reprovado.")
    print("Sua média é: ", "%.2f" % mediaPond)
elif (mediaPond >= 3) and (mediaPond <= 4.9):
    print("Recuperação.")
    print("Sua média é: ", "%.2f" % mediaPond)
else:
    print("Aprovado!")
    print("Sua média é: " "%.2f" % mediaPond)