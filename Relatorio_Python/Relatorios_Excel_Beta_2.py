import os
from pathlib import Path
import socket
import time
from procurar_planilha import procurar_planilha
from Enviar_email import Enviar_email
from Manual import manual
from alerta.alerta import alerta

def Relatorios_Excel_Beta_2():
    validar_ip = '000.000.000.0' # validar se o ip da maquina é o mesmo que o ip nesta variavel

    op = int('0')
    tentativa = int('0')
    HOST = 'google.com'
    PORT = 80

    while tentativa <= 3:
        try:
            s = socket.create_connection((HOST, PORT))
            print('Conexão estabelecida!')
            time.sleep(0.7)
            os.system('cls')
            s.close()
            break
        except socket.error as e:
            print('Problema com a conexão, tentando novamente...')
            tentativa = tentativa + 1
        time.sleep(1.2)

    # Checar o ip da maquina na rede
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    network_ip_address = s.getsockname()[0]
    s.close()

    if tentativa <= 5:
        if network_ip_address != validar_ip:
            while op != 4:
                print('<<<<Menu>>>>')
                print('1- Procurar pela planilha no dispositivo')
                print('2- Enviar relatório por e-mail')
                print('3- Manual')
                print('4- Sair')
                op = int(input('Opção: '))
                os.system('cls')
                if op == 1:
                    procurar_planilha()
                elif op == 2:
                    Enviar_email()
                elif op == 3:
                    manual()
                elif op == 4:
                    os.system('cls')
                    print('Saindo.')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Saindo..')
                    time.sleep(0.7)
                    os.system('cls')
                    print('Saindo...')
                    time.sleep(0.7)
        else:
            alerta()
    else:
        print('Sem conexão com a internet')