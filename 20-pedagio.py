import os
os.system("cls")

pedagio = input("Qual é o tipo do veículo: ").lower()  # transforma em minúscula

if pedagio == "carro":
    print("Você deve pagar 10 reais no pedágio")

elif pedagio == "moto":
    print("Você deve pagar 5 reais no pedágio")

elif pedagio == "caminhão":
    print("Você deve pagar 20 reais no pedágio")
 

else:
    print("Tipo de veículo inválido")

finalizacao = input("tenha uma boa viagem!")
