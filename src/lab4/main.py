from ClassOrdersParser import OrdersParser

def main(orders_filepath, order_country_filepath, non_valid_orders_filepath):
    """Функция для запуска обработки заказов """

    parser = OrdersParser(orders_filepath, order_country_filepath, non_valid_orders_filepath)
    parser.write_nonvalid_orders()
    parser.write_valid_orders()

if __name__ == "__main__":
    main("txtf/orders.txt", "txtf/order_country.txt", "txtf/non_valid_orders.txt")