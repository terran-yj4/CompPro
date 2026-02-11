import enum


n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b_d = dict()

for i, bi in enumerate(b):
    b_d[bi] = True

sum = 0
out_cnt = 0

# print(b_d)
for i, v in enumerate(a):
    # print(f"i: {i}, v: {v}")
    if b_d.get(i+1, False) and v < k:
        # print("アウト")
        out_cnt += 1
        sum += v

print(*[out_cnt, sum])