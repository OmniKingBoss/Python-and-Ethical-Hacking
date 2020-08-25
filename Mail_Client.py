import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.#MailProvider', 25)

server.ehlo()

with open('password.txt', 'r') as f:
	password = f.read()

server.login('mail', password)

msg = MIMEMultipart()
msg['From'] = 'OmniKingBoss'
msg['To'] = '#TargetMail'
msg['Subject'] = 'Just a test'


with open('message.txt', 'r') as f:
	message = f.read()


msg.attach(MIMEText(message, 'plain'))

filename = 'image.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail("yourmail", "targetmail", text)
