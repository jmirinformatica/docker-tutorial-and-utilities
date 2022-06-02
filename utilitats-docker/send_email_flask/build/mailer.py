import smtplib
import ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#https://realpython.com/python-send-email/
def envia_email(email_destinatari:str, titol:str, cos:str):

    email_origen = "no-respongueu@gmail.com"
    port = 587  # For starttls
    servidor_smtp = "smtp.gmail.com"
    password = "password-de-no-respongueu-gmail.com"

    print("------------------------------------------------------")
    print(f"From: {email_origen}")
    print(f"To: {email_destinatari}")
    print(f"Subject: {titol}")
    print(cos)
    print("------------------------------------------------------")

    missatge = MIMEMultipart("alternative")
    missatge["Subject"] = titol
    missatge["From"] = email_origen
    missatge["To"] = email_destinatari
    missatge.attach(MIMEText(cos, "plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP(servidor_smtp, port) as server:
        server.starttls(context=context)
        server.login(email_origen, password)
        server.sendmail(email_origen, email_destinatari, missatge.as_string())

    print("Mail enviat!")

################################################################################################
#
# Prova d'enviament d'emails
#
# envia_email(
#     email_destinatari = "email@del.client",
#     titol = "Hola!",
#     cos = "Això és una prova!\nEm reps?\nTot bé?"
# )
