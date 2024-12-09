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


def check_crosswords(grid):
    string_to_look_for = "MAS"

    occurrences = 0
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            # We only look for diagonals starting from the middle A, let's check there is room
            if i < 1 or j < 1:
                continue
            if i > len(line) - 2 or j > len(grid) - 2:
                continue
            if char != "A":
                continue

            # Check the diagonals
            if (sorted([grid[j - 1][i - 1], grid[j + 1][i + 1]]) == sorted("MS") and
                    sorted([grid[j - 1][i + 1], grid[j + 1][i - 1]]) == sorted("MS")):
                occurrences += 1

    return occurrences


def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


if __name__ == "__main__":
    print(check_crosswords(input_to_crosswords(get_input())))
