import os
os.system("cls")

print("bem vindo a calculadora")


n1 = float(input("digite o primeiro valor:"))
n2 = float(input("digite o segundo valor:"))

operacao = input("escolha a operação")


if(operacao == "+"):
    resultado = n1 + n2
    print("Resultado:", resultado)

elif (operacao == "-"):
    resultado = n1 - n2
    print("Resultado:", resultado)

elif (operacao == "*"):
    resultado = n1 * n2
    print("Resultado:", resultado)

elif (operacao == "/"):
    if n2 != 0:
        resultado = n1 / n2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print("Opção inválida.")
