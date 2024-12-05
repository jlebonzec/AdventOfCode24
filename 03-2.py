import re

RE_MULTS = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")

sample = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""


# That's a bad attempt from mo
def get_mults(input):
    lines = input.split("\n")
    split_by_dont = [e for l in lines for e in l.split("don't()")]
    split_by_do = [split_by_dont[0]] + [l.split("do()", 1)[1] for l in split_by_dont[1:] if "do()" in l]
    merged = "".join(split_by_do)

    return [list(map(int, s[4:-1].split(","))) for s in RE_MULTS.findall(merged)]


def get_total(input):
    total = 0
    enabled = True
    for m in RE_MULTS.findall(input):
        if m == "don't()":
            enabled = False
        elif m == "do()":
            enabled = True
        else:
            if enabled:
                x, y = list(map(int, m[4:-1].split(",")))
                total += x*y
    return total


def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


if __name__ == "__main__":
    print(get_total(get_input()))
