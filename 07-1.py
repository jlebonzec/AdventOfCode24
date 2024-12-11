import copy

sample = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

import re
import operator

RE_DIGITS = re.compile(r"\d+")
POSSIBLE_OPERATIONS = operator.add, operator.mul

def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


def process_input(input: str):
    return [line for line in input.strip().split("\n") if line]


def solve(lines):
    for line in lines:
        numbers = list(map(int, RE_DIGITS.findall(line)))
        result = numbers[0]
        step_results = [numbers[1]]
        for number in numbers[2:]:
            save = []
            for operation in POSSIBLE_OPERATIONS:
                for step_result in step_results:
                    save.append(operation(number, step_result))
            step_results = save
        if result in step_results:
            yield result


if __name__ == "__main__":
    print(sum(solve(process_input(get_input()))))
