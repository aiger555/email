import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from decouple import config


from_email = config('from_email',default='')
password = config('password',default='')


msg = MIMEMultipart()

to_email = 'nuralieva.aik@gmail.com'
message = 'Hi, it is a message with smtp!'

msg.attach(MIMEText(message, 'Homework'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, to_email, msg.as_string())
server.quit()