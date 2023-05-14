import pathlib
import typing as tp
import random

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
    return [values[i * n: (i + 1) * n] for i in range(n)]

    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row, col = pos
    result = []
    for i in range(len(grid)):
        result.append(grid[row][i])
    return result


    """Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row, col = pos
    result = []
    for i in range(len(grid)):
        result.append(grid[i][col])
    return result
    """Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    pass


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row, col = pos
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    block = []
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            block.append(grid[i][j])
    return block
    """Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """



def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                return i, j
    return None

    """Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    pass


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:

    """Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    row, col = pos
    values = set(str(i) for i in range(1, 10))

    for i in range(len(grid)):
        if grid[row][i] in values:
            values.remove(grid[row][i])
        if grid[i][col] in values:
            values.remove(grid[i][col])

    block_x = (row // 3) * 3
    block_y = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if grid[block_x + i][block_y + j] in values:
                values.remove(grid[block_x + i][block_y + j])

    return values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:

    """ Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """

    def find_empty(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
        for i in range(9):
            for j in range(9):
                if grid[i][j] == '.':
                    return i, j
        return None

    def is_valid(grid: tp.List[tp.List[str]], row: int, col: int, num: str) -> bool:
        if num in grid[row]:
            return False

        for i in range(9):
            if num == grid[i][col]:
                return False

        block_x = (row // 3) * 3
        block_y = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if num == grid[block_x + i][block_y + j]:
                    return False

        return True

    def solve_helper(grid: tp.List[tp.List[str]]) -> bool:
        empty = find_empty(grid)
        if empty is None:
            return True

        row, col = empty

        for k in range(1, 10):
            num = str(k)
            if is_valid(grid, row, col, num):
                grid[row][col] = num

                if solve_helper(grid):
                    return True

                grid[row][col] = '.'

        return False

    if solve_helper(grid):
        return grid
    else:
        return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """

    def is_valid(region: tp.List[str]) -> bool:
        # Проверяем, что все элементы уникальные, кроме нулей
        nums = set(region)
        nums.discard('.')
        return len(nums) == 9

    # Проверяем строки
    for row in solution:
        if not is_valid(row):
            return False

    # Проверяем столбцы
    for col in range(9):
        if not is_valid(solution[row][col] for row in range(9)):
            return False

    # Проверяем 3x3 квадраты
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = [solution[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
            if not is_valid(square):
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
    board = [['.' for _ in range(9)] for _ in range(9)]
    while count_numbers(board) < N:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != '.':
            continue
        num = str(random.randint(1, 9))
        if is_valid(board, row, col, num):
            board[row][col] = num
    return board

def is_valid(board: tp.List[tp.List[str]], row: int, col: int, num: str) -> bool:
    if num in board[row]:
        return False

    for i in range(9):
        if board[i][col] == num:
            return False

    r, c = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[r + i][c + j] == num:
                return False

    return True


def count_numbers(board: tp.List[tp.List[str]]) -> int:
    count = 0
    for row in board:
        for num in row:
            if num != '.':
                count += 1
    return count


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
