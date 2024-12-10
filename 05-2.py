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
import functools

PageList: TypeAlias = list[list[int]]
Order: TypeAlias = list[list[int]]


def process_input(input: str) -> tuple[Order, PageList]:
    order, pages = input.split("\n\n")
    order = [list(map(int, o.split("|"))) for o in order.split() if o]
    pages = [list(map(int, p.split(","))) for p in pages.split() if p]

    return order, pages


def verify_and_fix_ordering(order:Order, pages_list:PageList):
    dict_order = {}
    for first, second in order:
        if first not in dict_order:
            dict_order[first] = []
        dict_order[first].append(second)

    def compare(a, b):
        if b in dict_order.get(a, []):
            return -1
        if a in dict_order.get(b, []):
            return 1
        return 0

    total = 0
    for pages in pages_list:
        sorted_pages = sorted(pages, key=functools.cmp_to_key(compare))
        if sorted_pages != pages:
            total += sorted_pages[len(sorted_pages)//2]

    return total

def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.read()

    return content


if __name__ == "__main__":
    print(verify_and_fix_ordering(*process_input(get_input())))
