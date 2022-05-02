"""
25) Calcule as raízes da equeção de 2° grau;.
    Lembrando que:
    x = – b ± √∆ / 2∙a
        Onde:
    ∆ = b² - 4ac
    E ax² + bx + c = 0 representa uma equeção de 2° grau.
    A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem
    "Não é equação de segundo grau."
    - Se ∆ < 0, não existe real. Imprima a mensagem Não existe raiz
    - Se ∆ = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
    - Se ∆ > 0,imprima as duas raízes reais.
"""

A = float(input("Digite o valor da variável A: "))
B = float(input("Digite o valor da variável B: "))
C = float(input("Digite o valor da variável C: "))

if A != 0:
    delta = ((B ** 2) - (4 * A * C))
    if delta < 0:
        print("Não existe raiz.")
    elif delta == 0:
        X = (-B / (2 * A))
        print("Raíz única.")
        print("Raíz:", X)
    else:
        X1 = (-B + (delta ** 0.5) / (4 * A * C))
        X2 = (-B - (delta ** 0.5) / (4 * A * C))
        print("As duas raízes reais são:","%.2f" % X1, ",","%.2f" % X2)
else:
    print("Não é equação de segundo grau.")