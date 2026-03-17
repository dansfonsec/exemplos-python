import os
os.system("cls")


quantidade_de_produtos = float(input("Digite a quantidade do produto no estoque: "))
nome_do_produto = input("Digite o nome do produto: ")

if quantidade_de_produtos >= 5:
    print("Estoque está abaixo")
elif quantidade_de_produtos <= 6:
    print("Está tudo ok")