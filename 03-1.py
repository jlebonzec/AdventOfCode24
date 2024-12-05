import re

RE_MULTS = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

sample = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""


def get_mults(input):
    return [list(map(int, s[4:-1].split(","))) for s in RE_MULTS.findall(input)]


def get_total(input):
    return sum([i[0] * i[1] for i in get_mults(input)])


def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


if __name__ == "__main__":
    print(get_total(get_input()))
