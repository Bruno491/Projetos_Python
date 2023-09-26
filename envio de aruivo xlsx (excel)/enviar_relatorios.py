from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
import locale
import pyautogui

# Configuração do idioma para português
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Informações do e-mail
remetente = 'email_login'
senha = 'senha'
destinatarios = ['destino1@gmail.com', 'destino2@gmail.com']
assunto = f"Relatório {datetime.now().strftime('%B')} de {datetime.now().strftime('%Y')}"
corpo_email = f"Segue anexo relatório referente {datetime.now().strftime('%B')} de {datetime.now().strftime('%Y')}"

# Configuração do e-mail
msg = MIMEMultipart()
msg['From'] = remetente
msg['To'] = ', '.join(destinatarios)
msg['Subject'] = assunto
msg.attach(MIMEText(corpo_email, 'plain'))

# Anexar arquivo
filename = os.path.join("Caminho do arquivo", "relatorio.xlsx")
attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

# Enviar e-mail
server = smtplib.SMTP('smtp.outlook.com', 587)
server.starttls()
server.login(remetente, senha)
text = msg.as_string()
server.sendmail(remetente, destinatarios, text)
server.quit()

pyautogui.alert("Relatório enviado")
