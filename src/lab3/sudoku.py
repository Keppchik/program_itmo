import pathlib
import typing as tp

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    if grid == "No solutions":
        print("No solutions")
        return None

    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """Сгруппировать значения values в список, состоящий из списков по n элементов"""
    result = [[values[i] for i in range(n*j,n*(j+1))] for j in range(n)]
    return result


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row = grid[pos[0]]
    return row


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    col = [grid[i][pos[1]] for i in range(len(grid))]
    return col


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row = (pos[0]//3) * 3
    col = (pos[1]//3) * 3
    block = [grid[row+i][col+j] for i in range(3) for j in range(3)]
    return block


def find_empty_position(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                return row, col


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    possible_values = set()
    for value in "123456789":
        if value not in get_row(grid, pos) and value not in get_col(grid, pos) and value not in get_block(grid, pos):
            possible_values.add(value)
    return possible_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    pos = find_empty_position(grid)

    if pos is None:
        return grid

    values = find_possible_values(grid, pos)

    if values == set():
        return "No solutions"

    for value in values:
        grid[pos[0]][pos[1]] = value
        if solve(grid) == "No solutions":
            pass
        else:
            return grid
        grid[pos[0]][pos[1]] = "."

    return "No solutions"


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    for i in range(9):
        row = get_row(solution, (i,0))
        col = get_col(solution, (0,i))
        for number in "123456789":
            if number in row and number in col:
                pass
            else:
                return False
        for j in range(0,9,3):
            block = get_block(solution, (i,j))
            for number in "123456789":
                if number in block:
                    pass
                else:
                    return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    pass


if __name__ == "__main__":
    grid = read_sudoku('puzzle1.txt')
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)