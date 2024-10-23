import unittest
from src.lab3.sudoku import *

class SudokuTestCase(unittest.TestCase):

    def test_func_group(self):
        self.assertEquals(group([1,2,3,4], 2), [[1, 2], [3, 4]])
        self.assertEquals(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


