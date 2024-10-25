import unittest
from src.lab1_1.calculator import *

class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_add(self):
        self.assertEquals(Calculator().calc_add(12,5), 17)

    def test_minus(self):
        self.assertEquals(Calculator().calc_minus(12,5), 7)

    def test_multiply(self):
        self.assertEquals(Calculator().calc_multiply(12, 5), 60)

    def test_divide(self):
        self.assertEquals(Calculator().calc_divide(12,5), 2.4)