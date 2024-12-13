import os

from src.lab4.ClassOrder import Order


class OrdersParser:
    def __init__(self, orders_filepath, order_country_filepath, non_valid_orders_filepath):
        """ "Инициализирует объект OrdersParser"""

        self.orders_filepath = os.path.join(os.getcwd(), orders_filepath)
        self.order_country_filepath = os.path.join(os.getcwd(), order_country_filepath)
        self.non_valid_orders_filepath = os.path.join(os.getcwd(), non_valid_orders_filepath)
        self.orders = []
        self.make_orders()

    def make_orders(self):
        """Создаем массив классов заказов"""

        with open(self.orders_filepath, "r") as file:
            data = file.readlines()

            for line in data:
                line = line.split(";")
                if len(line) == 6:
                    self.orders.append(Order(line))

    def write_nonvalid_orders(self):
        """Записываем в файл все заказы, которые содержат ошибки
        Формат: <Номер заказа>;<Тип ошибки>;<Значение атрибута заказа, в котором содержится ошибка>"""

        with open(self.non_valid_orders_filepath, "w") as file:
            for order in self.orders:
                if order.errors:
                    for error in order.errors:
                        file.write(f"{order.number};{error[0]};{error[1]}\n")
                    file.write("\n")

    def write_valid_orders(self):
        """Записываем в файл все заказы без ошибок
        Формат: <Номер заказа>;<Набор продуктов>;<ФИО заказчика>;<Адрес доставки>;<Номер телефона>;<Приоритет доставки>"""

        self.orders.sort(
            key=lambda x: (
                0 if "Россия" in x.adress else 1,
                x.adress.split(". ")[0],
                0 if x.priority == "MAX" else 1 if x.priority == "MIDDLE" else 2,
            )
        )
        with open(self.order_country_filepath, "w") as file:
            for order in self.orders:
                if not order.errors:
                    products_string = ", ".join(
                        f"{product} x{quantity}" for product, quantity in order.compacted_products.items()
                    )
                    adress_list = order.adress.split(". ")[1:]
                    adress_string = ". ".join(adress_list)
                    order_string = f"{order.number};{products_string};{order.customer};{adress_string};{order.phone};{order.priority}"
                    file.write(order_string + "\n\n")
