from math import ceil, floor
n, m = map(int, input().split())

max_d = 0

for i in range(n):
    a, b = map(int, input().split())
    max_d = max(max_d, ceil((m-a) / b))

print(max_d)