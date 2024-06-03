from src.web_scrapp.service_order.get_orders import ServiceOrder
from src.web_scrapp.teams.send_message import MessageTeams
from src.send_email import MessageEmail


class App:
    def __init__(self):
        self.orders = 0
        self.teams_recipient = "lucas.vieira"
        self.email_recipient = self.teams_recipient + "@aguasdejoinville.com.br"

    def main(self):
        # Quantifica as ordens de chamado
        self.order()
        # Envia as mensagens
        self.send_message()

    def order(self):
        get_orders = ServiceOrder()
        self.orders = get_orders.main()

    def send_message(self):
        self.message_teams()
        self.message_email()

    def message_teams(self):
        send_message = MessageTeams(self.teams_recipient, self.orders)
        send_message.script()

    def message_email(self):
        send_message = MessageEmail(self.email_recipient, self.orders)
        send_message.main()


if __name__ == "__main__":
    app = App()
    app.main()
