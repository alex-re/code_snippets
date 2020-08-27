# https://www.youtube.com/watch?v=JRCJ6RtE3xU
# https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Emails/mail-demo.py

'''DON'T FORGET TO DO NOT NAME YOUR FILE email.py,BECAUSE IT WILL OVER RIDE DEFAULT MODULE'''

# myaccount.google.com/apppasswords

# export EMAIL='MyEmail'
# export EMAIL_PASSWORD='MyEmailPassword'


import smtplib
import os


SENDER_EMAIL = os.environ.get('EMAIL')
SENDER_EMAIL_TOKEN = os.environ.get('EMAIL_password')  # or EMAIL_PASSWORD
RECIVER_EMAIL = 'chalghoos1@gmail.com'


with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(SENDER_EMAIL, SENDER_EMAIL_TOKEN)

    subject = 'Hi from python'
    body = "don't name your file email.py!"

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(SENDER_EMAIL, RECIVER_EMAIL, msg)


''' localhost as smtp server '''

# in terminal:  `python3 -m smtpd -c DebuggingServer -n localhost:1025`

from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'Hi from python'
msg['From'] = SENDER_EMAIL
msg['To'] = RECIVER_EMAIL
msg.set_content("don't name your file email.py!")

with smtplib.SMTP('localhost', 1025) as smtp:
# with smtplib.SMTP_SSL('localhost', 465) as smtp:
    smtp.login(SENDER_EMAIL, SENDER_EMAIL_TOKEN)
    smtp.send_message(msg)


''' send Image '''
import imghdr

msg = EmailMessage()
msg['Subject'] = 'Image from python'
msg['From'] = SENDER_EMAIL
msg['To'] = RECIVER_EMAIL
msg.set_content("Image attached...")

files = ['image1.jpg', 'image2.jpg']

for file in files:
    with open(file, 'rb') as f:  # 'rb' -> read bytes
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    with smtplib.SMTP_SSL('localhost', 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_EMAIL_TOKEN)
        smtp.send_message(msg)


''' send pdf files '''

msg = EmailMessage()
msg['Subject'] = 'Pdf from python'
msg['From'] = SENDER_EMAIL
msg['To'] = RECIVER_EMAIL
msg.set_content("Pdf attached...")

files = ['file.pdf']

for file in files:
    with open(file, 'rb') as f:  # 'rb' -> read bytes
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('localhost', 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_EMAIL_TOKEN)
        smtp.send_message(msg)


''' send to more tha one contact '''
contacts = [RECIVER_EMAIL, 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Pdf from python'
msg['From'] = SENDER_EMAIL
msg['To'] = ', '.join(contacts)
msg.set_content("Pdf attached...")

files = ['file.pdf']

for file in files:
    with open(file, 'rb') as f:  # 'rb' -> read bytes
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    with smtplib.SMTP_SSL('localhost', 465) as smtp:
        smtp.login(SENDER_EMAIL, SENDER_EMAIL_TOKEN)
        smtp.send_message(msg)


''' send html '''

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'YourAddress@gmail.com'

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(SENDER_EMAIL, SENDER_EMAIL_TOKEN)
    smtp.send_message(msg)