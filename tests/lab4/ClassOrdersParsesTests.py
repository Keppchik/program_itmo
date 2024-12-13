import unittest

from src.lab4.ClassOrdersParser import OrdersParser


class ClassOrdersParserTestCase(unittest.TestCase):
    def setUp(self):
        self.parser = OrdersParser("orders_test.txt", "", "")

    def test_make_orders(self):
        self.assertEqual(
            str(self.parser.orders[0]),
            "1;Сыр;Анна;Россия. Ленинградская область. Санкт-Петербург. набережная реки Фонтанки;+7-921-456-78-90;MIDDLE;[]",
        )
        self.assertEqual(str(self.parser.orders[1]), "2;Молоко;Иван;;;MAX;[(2, 'no data'), (1, 'no data')]")
        self.assertEqual(
            str(self.parser.orders[2]),
            "3;Колбаса;Анна;Франция. Париж. Шанз-Элизе;+3-214-020-5-50;MIDDLE;[(2, '+3-214-020-5-50'), (1, 'Франция. Париж. Шанз-Элизе')]",
        )
        self.assertEqual(
            str(self.parser.orders[3]),
            "4;Хлеб;Мария;Германия. Бавария. Мюнхен. Мариенплац;+4-989-234-56;LOW;[(2, '+4-989-234-56')]",
        )
        self.assertEqual(
            str(self.parser.orders[4]),
            "5;Яблоки;Алексей;Италия. Рим. Колизей;+3-061-234-56-78;MAX;[(1, 'Италия. Рим. Колизей')]",
        )
