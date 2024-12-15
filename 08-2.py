sample = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

alphanum = "0123456789abcdefghijklmnopqrstuvwxyz"

def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


def process_input(input: str):
    # Grid is a dictionary of complex numbers to characters
    return {i+j*1j: c for j, r in enumerate(input.split("\n")) for i, c in enumerate(r.strip())}


def solve(grid):
    antennas = {c: [k for k, v in grid.items() if v == c] for c in set(grid.values()) if c != "."}
    antinodes = set()
    for antenna, positions in antennas.items():
        for a in positions:
            for b in positions:
                if a == b:
                    continue
                antinodes |= {a+n*(a-b) for n in range(50)}

    return len(antinodes & {*grid})


if __name__ == "__main__":
    print(solve(process_input(sample)))
    print(solve(process_input(get_input())))
