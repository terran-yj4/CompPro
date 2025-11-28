from itertools import groupby

S = list(map(int, list(input())))

a = [[key,len(list(group))] for key,group in groupby(S)]

prev_n = -1
prev_cnt = 0
cnt = 0

for item in a:
    if prev_n + 1 == item[0]:
        cnt += min(prev_cnt, item[1])
        prev_cnt = item[1]

    prev_n = item[0]
    prev_cnt = item[1]

print(cnt)
