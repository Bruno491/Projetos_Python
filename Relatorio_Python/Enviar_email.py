import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
from listas.lista_departamentos import lista_departamentos

def Enviar_email():
    email = ""
    password = ""
    if os.path.exists("C:\\restante_do_caminho\\usuario.txt"):
        with open("C:\\restante_do_caminho\\usuario.txt", "r") as f:
            users = f.read().splitlines()

        for user in users:
            email = user.split(":")[0]
            password = user.split(":")[1]
    
    smtp_server = f'smtp.outlook.com'
    smtp_port = 587
    smtp_username = email
    smtp_password = password
    from_address = smtp_username
    to_address = str(lista_departamentos())
    
    # Cria a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = input("Informe o assunto so e-mail: ")
    os.system('cls')
    
    # Adiciona o texto da mensagem
    body = input('Informe sua mensagem: ')
    msg.attach(MIMEText(body, 'plain'))
    os.system('cls')
    
    # Adiciona o arquivo anexado
    nome = input('Informe o nome do arquivo: ')
    os.system('cls')
        
    if os.path.isfile(f'C:\\restante_do_caminho\\{nome}.xlsx'):
        filename = (f'C:\\restante_do_caminho\\{nome}.xlsx')
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=(f'{nome}.xlsx'))
        msg.attach(part)
                
    elif os.path.isfile(f'C:\\restante_do_caminho\\{nome}.xlsx'):
        filename = (f'C:\\restante_do_caminho\\{nome}.xlsx')
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=(f'{nome}.xlsx'))
        msg.attach(part)
            
    elif os.path.isfile(f'C:\\restante_do_caminho\\{nome}.xlsx'):
        filename = (f'C:\\restante_do_caminho\\{nome}.xlsx')
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=(f'{nome}.xlsx'))
        msg.attach(part)

    # Conecta-se ao servidor SMTP e envia a mensagem
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
    print('Email enviado')
    os.system('pause')
    os.system('cls')