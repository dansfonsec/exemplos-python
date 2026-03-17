import os
os.system("cls")

print("===== BOLETIM ESCOLAR =====")

# Nome do aluno
nome = input("Digite o nome do aluno: ")

# Notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

print("\n===== RESULTADO =====")
print("Aluno:", nome)
print("Média:", round(media, 2))

# Verificação de aprovação
if media >= 7:
    print("Situação: Aprovado")
elif media >= 5:
    print("Situação: Recuperação")
else:
    print("Você está reprovado")