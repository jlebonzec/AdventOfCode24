import copy

unusual_data = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]


def is_sorted(line):
    return sorted(line) == line or sorted(line, reverse=True) == line


def has_small_gaps(line):
    return all(1 <= abs(line[i] - line[i + 1]) <= 3 for i in range(len(line) - 1))


def is_safe(line):
    for i in range(len(line)):
        tampered = copy.deepcopy(line)
        del tampered[i]
        if is_sorted(tampered) and has_small_gaps(tampered):
            return True
    return False


def count_safe(data):
    return sum(is_safe(line) for line in data)


def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.readlines()

    return [list(map(int, i.split())) for i in content]


if __name__ == "__main__":
    print(count_safe(get_input()))
