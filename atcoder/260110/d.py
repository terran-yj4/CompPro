"""未完成"""

import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
    X, Y = map(int, input().split())

    # X <= A[i] <= X+Y の個数
    left = bisect.bisect_left(A, X)
    right = bisect.bisect_right(A, X + Y)

    cnt = right - left
    print(X+Y+cnt)
