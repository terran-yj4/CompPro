from math import lcm
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# N, X, Y = 3, 6, 8
# A = [11, 10, 13]

# N, X, Y = 2, 3, 4
# A = [3, 5]

# N, X, Y = 8, 4, 32
# A = [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]


# print(N, X, Y)
# print(A)

# 最小公倍数
lcm_ = lcm(X, Y)
kgr_ = lcm(X, Y) // Y

# print(f"最小公倍数: {lcm_}")
# print(f"区切り:     {kgr_}")

isOk = True

r = (A[0] * X) % (m:=(Y - X))
for a in A:
    if a*X % m != r:
        isOk = False

max_xY = list(a * Y for a in A)

# print(f"max_xY: {max_xY}")
min_xY = min(max_xY)

sum = 0
if isOk:
    for a in A:
        # n = a - (a * Y - min_xY) // (Y - X)
        n = (min_xY - a * X) // (Y - X)
        # print(n, a * Y - min_xY, Y-X)
        if n >= 0:
            sum += n
        else:
            isOk = False
            break

if isOk:
    print(sum)
else:
    print(-1)
