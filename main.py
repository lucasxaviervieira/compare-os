from src.web_scrapp.service_order import get_orders as go
from src.web_scrapp.teams import send_message as mt
from src import send_email as me


class App:
    def __init__(self):
        self.orders = 0

    def main(self):
        self.order()
        self.send_message()

    def order(self):
        get_orders = go.ServiceOrder()
        self.orders = get_orders.main()

    def send_message(self):
        self.message_teams()
        self.message_email()

    def message_teams(self):
        teams_provisory_recipient = "osvaldo.silva"
        send_message = mt.MessageTeams(teams_provisory_recipient, self.orders)
        send_message.script()

    def message_email(self):
        email_provisory_recipient = "lucas.vieira@aguasdejoinville.com.br"
        send_message = me.MessageEmail(email_provisory_recipient, self.orders)
        send_message.main()


if __name__ == "__main__":
    app = App()
    app.main()
