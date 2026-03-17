import os
os.system("cls")
print("bem vindo ao program de imc!")

peso = float(input("digite sue peso em KG:"))
altura = float(input("digite sua altura em metros"))


imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc <= 16.9:
    print("Você está muito abaixo do peso")
elif 17 <= imc <= 18.4:
    print("Você está abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Você está no peso ideal")
elif 25 <= imc <= 29.9:
    print("Você está acima do peso")
elif 30 <= imc <= 34.9:
    print("imenso d+")
elif 35 <= imc <= 39.9:
    print("branca de neve e 7 refeições kkkk")
else:  # imc >= 40
    print("apenas desista")