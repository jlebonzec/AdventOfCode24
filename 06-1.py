sample = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


def process_input(input: str):
    mapping = [list(line) for line in input.strip().split("\n")]
    return mapping


DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

TURN_90_DEGREES_RIGHT = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}


def move(mapping):
    for i, line in enumerate(mapping):
        for j, char in enumerate(line):
            if char not in DIRECTIONS:
                continue

            mapping[i][j] = "X"

            if i + DIRECTIONS[char][0] < 0 or i + DIRECTIONS[char][0] >= len(mapping) or j + DIRECTIONS[char][1] < 0 or j + DIRECTIONS[char][1] >= len(line):
                raise IndexError("Out of bounds")

            next = mapping[i + DIRECTIONS[char][0]][j + DIRECTIONS[char][1]]
            if next == "#":  # Turn 90 degrees right
                mapping[i][j] = TURN_90_DEGREES_RIGHT[char]
                mapping = move(mapping)
            elif next in (".", "X"):  # Continue moving
                mapping[i + DIRECTIONS[char][0]][j + DIRECTIONS[char][1]] = char

            return mapping
    return mapping


def move_forever(mapping, animate=True):
    try:
        while True:
            move(mapping)

    except IndexError:
        return mapping


def count_crossed_tiles(mapping):
    return sum(line.count("X") for line in mapping)


if __name__ == "__main__":
    print(count_crossed_tiles(move_forever(process_input(sample))))
    print(count_crossed_tiles(move_forever(process_input(get_input()))))
