"""Importing modules"""
import multiprocessing
import pathlib
import time
import typing as tp
from random import randint

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open(encoding="utf-8") as file:
        puzzle = file.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    """Преобразует файл с судоку в список"""
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    if grid is None:
        print("No solutions")
        return None

    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print("".join(grid[row][col].center(width) + \
                      ("|" if str(col) in "25" else "") for col in range(9)))
        if str(row) in "25":
            print(line)
    print()
    return None


def group(values: tp.List[T], length: int) -> tp.List[tp.List[T]]:
    """Сгруппировать значения values в список, состоящий из списков по length элементов"""
    result = [[values[i] for i in range(length * j, length * (j + 1))] for j in range(length)]
    return result


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает строку по позиции"""
    row = grid[pos[0]]
    return row


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает столбец по позиции"""
    col = [grid[i][pos[1]] for i in range(len(grid))]
    return col


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает блок 3х3 по позиции"""
    row = (pos[0] // 3) * 3
    col = (pos[1] // 3) * 3
    block = [grid[row + i][col + j] for i in range(3) for j in range(3)]
    return block


def find_empty_position(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Находит первую позицию точки"""
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                return row, col
    return None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Находит все возможные значения для определенной позиции"""
    possible_values = set()
    for value in "123456789":
        if value not in get_row(grid, pos) and value not in get_col(grid, pos) \
                and value not in get_block(grid, pos):
            possible_values.add(value)
    return possible_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решает судоку методом перебора с возвратом"""
    pos = find_empty_position(grid)

    if pos is None:
        return grid

    values = find_possible_values(grid, pos)

    if values == set():
        return None

    for value in values:
        grid[pos[0]][pos[1]] = value
        if solve(grid):
            return grid
        grid[pos[0]][pos[1]] = "."

    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Проверяет правильно ли решена судоку и решена ли вообще"""
    for i in range(9):
        row = get_row(solution, (i, 0))
        col = get_col(solution, (0, i))
        for number in "123456789":
            if number in row and number in col:
                pass
            else:
                return False
        for j in range(0, 9, 3):
            block = get_block(solution, (i, j))
            for number in "123456789":
                if number in block:
                    pass
                else:
                    return False
    return True


def generate_sudoku(amount: int) -> tp.List[tp.List[str]]:
    """Создает сетку судоку с amount количеством цифр"""
    grid = [["."] * 9 for _ in range(9)]

    solved_grid = solve(grid)
    if solved_grid is None:
        raise ValueError("Не удалось сгенерировать решенную сетку судоку")

    grid = solved_grid

    positions_of_numbers = []
    for _ in range(81 - amount):
        row, col = randint(0, 8), randint(0, 8)
        while (row, col) in positions_of_numbers:
            row, col = randint(0, 8), randint(0, 8)
        positions_of_numbers.append((row, col))
        grid[row][col] = "."

    return grid


def run_solve(file: str) -> None:
    """Засекает время, за которон решается судоку, и запускает решение"""
    grid = read_sudoku(file)
    start = time.time()
    solution = solve(grid)
    end = time.time()
    if not solution:
        print(f"Puzzle {file} can't be solved")
    else:
        display(solution)
        print(f"{file}: {end-start} \n")


if __name__ == "__main__":
    for file_name in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        p = multiprocessing.Process(target=run_solve, args=(file_name,))
        p.start()
