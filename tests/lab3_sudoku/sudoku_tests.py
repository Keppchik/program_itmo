import unittest
from src.lab3.sudoku import *

class SudokuTestCase(unittest.TestCase):
    def test_func_group(self):
        self.assertEquals(group([1,2,3,4], 2), [[1, 2], [3, 4]])
        self.assertEquals(group([1,2,3,4,5,6,7,8,9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_func_get_row(self):
        self.assertEquals(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)),['1', '2', '.'])
        self.assertEquals(get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0)),['4', '.', '6'])
        self.assertEquals(get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0)),['.', '8', '9'])

    def test_func_get_col(self):
        self.assertEquals(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)),['1', '4', '7'])
        self.assertEquals(get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1)),['2', '.', '8'])
        self.assertEquals(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), ['3', '6', '9'])

    def test_func_get_block(self):
        grid = read_sudoku("test_puzzle.txt")
        self.assertEquals(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])
        self.assertEquals(get_block(grid, (4,7)),['.', '.', '3', '.', '.', '1', '.', '.', '6'])
        self.assertEquals(get_block(grid, (8, 8)),['2', '8', '.', '.', '.', '5', '.', '7', '9'])