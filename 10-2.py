sample = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def add_tuples(a, b):
    return tuple(map(sum, zip(a, b)))

def get_neighbours(pos):
    return [add_tuples(pos, d) for d in DIRECTIONS]

def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


def process_input(input: str):
    return {(i, j): int(c) for i, r in enumerate(input.split("\n")) for j, c in enumerate(r.strip())}


def solve(mapping):
    trails = {pos: 0 for pos, digit in mapping.items() if digit == 0}
    for pos in trails:
        # Using lists instead of sets, we purposely add duplicates representing possible paths
        options = [pos]
        for i in range(1, 10):
            alternatives = []
            for option in options:
                for neighboor in get_neighbours(option):
                    if neighboor in mapping and mapping[neighboor] == i:
                        alternatives.append(neighboor)
            options = list(alternatives)
        trails[pos] += len(options)

    return sum(trails.values())


if __name__ == "__main__":
    assert solve(process_input(sample)) == 81
    print(solve(process_input(get_input())))
