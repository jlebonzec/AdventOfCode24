sample = """
12345
"""

def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


def process_input(input: str):
    # Grid is a dictionary of complex numbers to characters
    return list(map(int, input.strip()))


def solve(disk_map):
    layout = []
    for i, digit in enumerate(disk_map):
        if i % 2 == 0:  # even, it's a file, so we compute its id and add it to the layout
            layout += [i // 2] * digit
            continue

        # It's odd, so we want to fetch the latest file id and add it to the layout
        for j in range(digit):
            while disk_map[-1] == 0 or len(disk_map) % 2 == 0:  # If empty or odd (e.g. a space), we pop it
                disk_map.pop()
            if i >= len(disk_map):  # We've reduced the disk size enough to be done
                break
            layout.append(len(disk_map) // 2)
            disk_map[-1] -= 1  # We have one less chunk of that file to move

    return sum([i * j for i, j in enumerate(layout)])


if __name__ == "__main__":
    assert solve(process_input("12345")) == 60
    assert solve(process_input("2333133121414131402")) == 1928
    print(solve(process_input(get_input())))
