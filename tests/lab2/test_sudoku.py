import unittest
from src.lab2.sudoku import *

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

    def test_func_find_empty_position(self):
        self.assertEquals(find_empty_position([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]), (0, 2))
        self.assertEquals(find_empty_position([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]), (1, 1))
        self.assertEquals(find_empty_position([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']]), (2, 0))

    def test_func_find_possible_values(self):
        grid = read_sudoku("test_puzzle.txt")
        self.assertEquals(find_possible_values(grid, (0, 2)),{'1', '2', '4'})
        self.assertEquals(find_possible_values(grid, (4, 7)), {'2', '5', '9'})

    def test_func_solve(self):
        grid = read_sudoku("test_puzzle.txt")
        self.assertEquals(solve(grid),[['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']])

    def test_func_check_solution(self):
        self.assertEquals(check_solution([['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]), True)
        self.assertEquals(check_solution([['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['5', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]), False)
        self.assertEquals(check_solution([['5', '5', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]), False)

    def test_func_generate_grid(self):
        grid = generate_sudoku(40)
        self.assertEquals(sum(1 for row in grid for e in row if e == '.'), 41)
        grid = generate_sudoku(1000)
        self.assertEquals(sum(1 for row in grid for e in row if e == '.'), 0)
        grid = generate_sudoku(0)
        self.assertEquals(sum(1 for row in grid for e in row if e == '.'), 81)