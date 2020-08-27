'''DON'T FORGET TO DO NOT NAME YOUR FILE email.py,BECAUSE IT WILL OVER RIDE DEFAULT MODULE'''
# myaccount.google.com/apppasswords
# export EMAIL='MyEmail'
# export EMAIL_PASSWORD='MyEmailPassword'

import smtplib
import os



SENDER_EMAIL = os.environ.get('EMAIL')
SENDER_EMAIL_TOKEN = os.environ.get('EMAIL_password')
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
