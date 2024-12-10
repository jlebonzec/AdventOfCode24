sample = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

from typing import TypeAlias
from collections import namedtuple

PageList: TypeAlias = list[list[int]]
Order: TypeAlias = list[list[int]]


def process_input(input: str) -> tuple[Order, PageList]:
    order, pages = input.split("\n\n")
    order = [list(map(int, o.split("|"))) for o in order.split() if o]
    pages = [list(map(int, p.split(","))) for p in pages.split() if p]

    return order, pages


def verify_ordering(order:Order, pages_list:PageList):
    total = 0
    for pages in pages_list:
        seen = set()
        for page in pages:
            for o in order:
                if o[0] == page:
                    if o[1] in seen:
                        break
            else:
                seen.add(page)
                continue
            break
        else:
            total += pages[len(pages)//2]

    return total

def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


if __name__ == "__main__":
    print(verify_ordering(*process_input(get_input())))
