"""
22) Leia a idade e o tempo de serviço de um trabalhador e escreva
se ele pode ou não se aposentar. As condições para posentadoria são
    - Ter pelo menos 64,
    - Ou ter trabalhado pelo menos 30 anos,
    - Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos
"""

idade = int(input("Digite uma idade: "))
tempServ = int(input("Digite o tempo de serviço: "))

if (idade >= 64) or (tempServ >= 30):
    print("Pode se aposentar.")
elif (idade >= 60) and (tempServ >= 25):
    print("Pode se aposentar.")
else:
    print("Não pode se aposentar.")
