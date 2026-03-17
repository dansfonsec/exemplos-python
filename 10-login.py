import os
os.system("cls")

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite a senha: ")
 
if usuario == "admin" and senha == "123":
    print("Acesso liberado")
   
else:print("Acesso negado")
