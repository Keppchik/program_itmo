import unittest

from src.lab4.ClassOrder import Order


class ClassOrderTestCase(unittest.TestCase):
    def setUp(self):
        self.good_order = Order(
            [
                "31987",
                "Сыр, Колбаса, Сыр, Макароны, Колбаса",
                "Петрова Анна",
                "Россия. Ленинградская область. Санкт-Петербург. набережная реки Фонтанки",
                "+7-921-456-78-90",
                "MIDDLE",
            ]
        )
        self.bad_order = Order(
            [
                "84756",
                "Печенье, Сыр, Печенье, Сыр",
                "Васильева Анна Владимировна",
                "Япония. Шибуя. Шибуя-кроссинг",
                "+8-131-234-5678",
                "MAX",
            ]
        )

    def test_is_valid(self):
        self.assertEquals(self.good_order.errors, [])
        self.assertEquals(self.bad_order.errors, [(2, "+8-131-234-5678"), (1, "Япония. Шибуя. Шибуя-кроссинг")])

    def test_compact_products(self):
        self.assertEquals(self.good_order.compacted_products, {"Сыр": 2, "Колбаса": 2, "Макароны": 1})
        self.assertEquals(self.bad_order.compacted_products, {"Печенье": 2, "Сыр": 2})
