"""
11) Escreva um programa que leia um número inteiro maior do que zero
e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número
251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que
zero, programa terminará com a mensagem 'Número inválido'
"""

num = int(input("Digite um número: "))

if num > 0:
    num = str(num)
    soma = 0
    for i in range(len(num)):
        soma += int(num[i])

    print("A soma dos algarísmos é:", soma)
else:
    print("Número Inválido.")