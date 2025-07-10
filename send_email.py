import smtplib, ssl

def send_email(subject, body, sender_email, receiver_email, password):
        host = "smtp.gmail.com"
        port = 465

        message = f"Subject: {subject}\nFrom: {sender_email}\nTo: {receiver_email}\n\n{body}"

        context = ssl.create_default_context()
        try:
                with smtplib.SMTP_SSL(host, port, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, message)
                return True
        except Exception as e:
                print(f"Error sending email: {e}")
                return False
