import smtplib, ssl
import os
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "k214944@nu.edu.pk"
    password = "arbqcygvftwvdapp"

    reciever = "k214944@nu.edu.pk"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

    print("Email was sent!")