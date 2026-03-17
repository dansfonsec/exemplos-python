import os
os.system("cls")
boas_vindas = input("seja bem vindo! ")
quantidade_de_letras = input("Digite uma frase para contar as letras: ")

quantidade = len(quantidade_de_letras.replace("", ""))
print("quantidade de letras:", quantidade)
