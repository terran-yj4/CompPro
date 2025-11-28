N = int(input())

A = list(map(int, input().split()))
elems_cnt = len(A)
elem_dict = {}
for item in A:
    if item not in elem_dict.keys():
        elem_dict[item] = 1
    else:
        elem_dict[item] += 1
# print(elem_dict)
# print(elem_dict.values())

a_cnt = 0
for key, num_cnt in elem_dict.items():
    if num_cnt >= 2:
        this_pattern = num_cnt * (num_cnt-1) / 2
        other_pattern = N - num_cnt
        a_cnt += this_pattern * other_pattern

print(int(a_cnt))