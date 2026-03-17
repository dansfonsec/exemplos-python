import os
os.system("cls")


placa_do_carro = input("digite a placa do carro:")
velocidade = float(input("digite a velocidade:"))

if velocidade >= 80:
    print("voce esta acima do limite permitido, voçê esta multado") 

elif velocidade <= 79:
    print("voçê esta dentro do limite permitido")
