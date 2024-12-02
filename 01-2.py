left_list = [3,4,2,1,3,3]
right_list = [4,3,5,3,9,3]

def get_distance(left_list, right_list):
    t = zip(sorted(left_list), sorted(right_list))
    return sum(abs(x-y) for x,y in t)

def get_similarity(left_list, right_list):
    occ_map = {}
    for i in right_list:
        if i not in occ_map:
            occ_map[i] = 1
        else:
            occ_map[i] += 1

    return sum([i * occ_map.get(i,0) for i in left_list if i in occ_map])

def get_input():
    self_path = __file__
    input_path = f"{'/'.join(self_path.split('/')[:-1])}/inputs/{self_path.split('/')[-1].split('.')[0].split('-')[0]}.txt"
    with open(input_path, 'r') as f:
        content = f.readlines()

    left_list = [int(i.split()[0]) for i in content]
    right_list = [int(i.split()[1]) for i in content]

    return left_list, right_list


if __name__ == "__main__":
    print(get_distance(*get_input()))
    print(get_similarity(*get_input()))
