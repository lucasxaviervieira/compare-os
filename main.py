from src.web_scrapp.service_order import get_orders as go
from src.web_scrapp.teams import send_message as sm


class App:
    def __init__(self) -> None:
        pass

    def main(self):
        self.order()
        self.send_message()

    def order(self):
        get_orders = go.ServiceOrder()
        self.orders = get_orders.main()

    def send_message(self):
        send_message = sm.MessageTeams(self.orders)
        send_message.script()


if __name__ == "__main__":
    app = App()
    app.main()
