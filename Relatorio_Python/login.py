import sys
import os
from Relatorios_Excel_Beta_2 import Relatorios_Excel_Beta_2

# Obter o email e a senha do usuário
email = input("Email: ")
password = input("Senha: ")

# Verificar se existe arquivo com as credenciais
if os.path.exists("C:\\Users\\bruno\\OneDrive\\Documentos\\usuario.txt"):
    # Verificar se as credenciais do usuário estão corretas
    with open("C:\\Users\\bruno\\OneDrive\\Documentos\\usuario.txt", "r") as f:
        users = f.read().splitlines()

    for user in users:
        if user.split(":")[0] == email and user.split(":")[1] == password:
            print("Bem vindo!")
            Relatorios_Excel_Beta_2()
            break
    else:
        print("Email e/ou senha invalido!")
else:
    #melhorar essa opção
    print("Usuario não encontrado! Por favor conta uma conta.")
    # Criar novo ususario
    if input("Deseja criar uma conta? (S/N): ") == "S":
        with open("C:\\Users\\bruno\\OneDrive\\Documentos\\usuario.txt", "a") as f:
            f.write(email + ":" + password + "\n")
        print("Conta registrada com sucesso!")