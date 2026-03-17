import os
os.system("cls")


usuario = input("Digite seu nome:")
tempo_de_estudo = int(input("Digite quantas horas voçê estuda por dia:"))

if tempo_de_estudo <= 2:
    print("pouco tempo de estudo")

elif tempo_de_estudo < 4:
    print("tempo medio de estudo")

else:
    print("muito tempo de estudo")