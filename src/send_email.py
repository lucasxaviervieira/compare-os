import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src import secret as sct


class MessageEmail:
    def __init__(self, email_recipient, orders):
        self.email_recipient = email_recipient
        self.orders = orders

    def main(self):
        self.get_password()
        self.send_email()

    def get_password(self):
        secret_manager = sct.Secret()
        self.email_sender, self.password = secret_manager.email_manager()

    def send_email(self):
        msg = MIMEMultipart()

        message = f"Quantidade de Licenças: {self.orders}"

        msg["From"] = self.email_sender
        msg["To"] = self.email_recipient
        msg["Subject"] = "Alerta OS"

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", port=587)

        server.starttls()

        server.login(msg["From"], self.password)

        server.sendmail(msg["From"], msg["To"], msg.as_string())

        server.quit()
