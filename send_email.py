import smtplib, ssl

# from pages.Contact_Me import message

host = "smtp.gmail.com"
port = 465


username = "osanchez.python@gmail.com"
password = "dhmu kggi jrzh azje"

receiver = "osanchez.python@gmail.com"
context = ssl.create_default_context()

message = '''\
Subject: Hi!
How are you?
Bye!
'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)