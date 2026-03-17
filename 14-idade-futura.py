import os
os.system("cls") 

nome = input("Digite seu nome: ")

idade_atual = int(input("Digite sua idade atual: "))

ano_atual = 2026
ano_futuro = 2035


idade_futura = idade_atual + (ano_futuro - ano_atual)


print(f"{nome}, em {ano_futuro} você terá {idade_futura} anos.")