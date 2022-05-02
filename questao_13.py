"""
13) Faça um algoritmo que calcule a média ponderada das notas de 3 provas.
A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final,
mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))

mediaPond = ((nota1 * 1) + (nota2 * 1) + (nota3 * 2)) / 4

if mediaPond >= 6:
    print("A média do aluno é:", "%.2f" % mediaPond)
    print("Aprovado!")
else:
    print("A média do aluno é:", "%.2f" % mediaPond)
    print("Reprovado.")
