import os
os.system("cls")

nivel = int(input("Digite o nível do professor (1, 2 ou 3): "))
aulas = int(input("Digite a quantidade de aulas por semana: "))


if nivel == 1:
    valor_hora = 12
elif nivel == 2:
    valor_hora = 17
elif nivel == 3:
    valor_hora = 25
else:
    print("Nível inválido!")
    valor_hora = 0


salario = aulas * valor_hora


print("Salário do professor: R$", salario)