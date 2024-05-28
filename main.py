from src.web_scrapp.service_order import get_orders as go


def main():
    get_orders = go.ServiceOrder()
    get_orders.script()


if __name__ == "__main__":
    main()
