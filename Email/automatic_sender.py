import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

smtp_server = 'smtp.abv.bg'
port = 465
sender_email = 'ivan.krasenov7@abv.bg'
sender_password = ''
receiver_email = 'teodorkolev@yahoo.com'
subject = 'Test Email from Tedy'

message = 'This is a test email from Tedy sent with Python'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

msg.attach(MIMEText(message, 'plain'))

attachment_file = '/age1.png'

with open(attachment_file, 'rb') as file:
    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="{attachment_file}"')
    msg.attach(attachment)

try:
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(user=sender_email, password=sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email was sent successfully")

except Exception as e:
    print(str(e))
