import os
os.system("cls")

def dividir(conta, tp):
    return conta / tp

def encerrar_programa():
    input("\nPressione Enter para finalizar...")

print("=== Seja bem-vindo ao App Minha Conta ===\n")

conta = float(input("Qual foi o valor da conta: R$ "))
tp = int(input("Digite o total de pessoas: "))


resultado = dividir(conta, tp)

print("\n--- Resultado ---")
print(f"Total da conta: R$ {conta:.2f}")
print(f"Número de pessoas: {tp}")
print(f"Valor por pessoa: R$ {resultado:.2f}")


encerrar_programa()