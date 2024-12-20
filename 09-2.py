sample = """
12345
"""

from collections import deque


def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


def process_input(input: str):
    # Grid is a dictionary of complex numbers to characters
    return list(map(int, input.strip()))


# Solution from 4HbQ
class Mem():
    def __init__(b, pos, len): b.pos = pos; b.len = len
    def val(b): return (2*b.pos + b.len-1) * b.len // 2


def solve(disk_map):
    pos, mem = 0, []
    for len in disk_map:
        mem += [Mem(pos, len)]
        pos += len

    for used in mem[::-2]:
        for free in mem[1::2]:
            if (free.pos <= used.pos
            and free.len >= used.len):
                used.pos  = free.pos
                free.pos += used.len
                free.len -= used.len

    return sum(id*m.val() for id, m in enumerate(mem[::2]))


if __name__ == "__main__":
    print(solve(process_input("2333133121414131402")))
    print(solve(process_input(get_input())))
