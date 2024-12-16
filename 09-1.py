sample = """
2333133121414131402
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
    zeroes = 0
    for i, digit in enumerate(disk_map):
        if i % 2 == 0:
            layout += [i // 2] * digit
            continue
        zeroes += digit
        for j in range(digit):
            while disk_map[-1] == 0 or len(disk_map) % 2 == 0:
                zeroes += disk_map.pop()
            layout.append(len(disk_map) // 2)
            disk_map[-1] -= 1

    print("".join(list(map(str, layout))) + "." * zeroes)

    return sum([i * j for i, j in enumerate(layout)])


if __name__ == "__main__":
    print(solve(process_input(sample)))
    # print(solve(process_input(get_input())))
