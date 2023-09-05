from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import socket
import os

def alerta():
    email = 'teste_email@outlook.com'
    senha = 'testes_Senha'
    titulo = 'Acesso não autorizado'
    username = os.getlogin()
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    network_ip_address = s.getsockname()[0]
    s.close()
    
    # Configurações do servidor SMTP e do remetente
    smtp_server = 'smtp.outlook.com'
    smtp_port = 587
    smtp_username = email
    smtp_password = senha
    from_address = smtp_username
    to_address = email
    
    # Cria a mensagem
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = titulo
    
    # Adiciona o texto da mensagem
    body = f'Uma tentativa de acesso foi detectada em um equipamento não autorizado. Ip do equipamento: {network_ip_address}. Usuario que tentou acesso: {username}'
    msg.attach(MIMEText(body, 'plain'))
    
    # Conecta-se ao servidor SMTP e envia a mensagem
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
    print('Acesso negado')