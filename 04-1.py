sample = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

from typing import TypeAlias

Grid: TypeAlias = list[list[str]]
Crosswords: TypeAlias = list[str]


def input_to_crosswords(input: str) -> Crosswords:
    return input.strip().split('\n')


def grid_get_diagonal(grid: Crosswords) -> Crosswords:
    """ Returns the diagonals of the grid, filling with spaces """
    size = len(grid)
    diags = [[" "] * size for i in range(size * 2 - 1)]
    if len(grid[0]) != size:
        raise ValueError("Grid is not square")
    for i in range(size):
        for j in range(size):
            diags[i + j][i] = grid[j][i]
    return ["".join(line) for line in diags]


def grid_mirror(grid: Crosswords) -> Crosswords:
    """ Flips the grid horizontally """
    return [line[-1::-1] for line in grid]


def grid_mirror_vertical(grid: Crosswords) -> Crosswords:
    """ Flips the grid vertically """
    return grid[-1::-1]


def grid_rotate_90(grid: Crosswords) -> Crosswords:
    """ Rotates the grid 90 degrees """
    return ["".join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]) - 1, -1, -1)]


def get_alternate_grids(grid: Crosswords) -> list[Crosswords]:
    mirrored = grid_mirror(grid)
    rotated_90 = grid_rotate_90(grid)
    rotated_270 = grid_mirror(rotated_90)
    diag = grid_get_diagonal(grid)
    diag_mirrored = grid_get_diagonal(mirrored)
    diag_mirrored_vertical = grid_get_diagonal(grid_mirror_vertical(grid))
    diag_rotated_180 = grid_get_diagonal(grid_mirror_vertical(mirrored))
    return [
        grid,
        mirrored,
        rotated_90,
        rotated_270,
        diag,
        diag_mirrored,
        diag_mirrored_vertical,
        diag_rotated_180
    ]


def check_crosswords(grid):
    string_to_look_for = "XMAS"
    grids = get_alternate_grids(grid)
    occurrences = 0
    for alternative in grids:
        for line in alternative:
            occurrences += line.count(string_to_look_for)
    return occurrences


def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


if __name__ == "__main__":
    print(check_crosswords(input_to_crosswords(get_input())))
