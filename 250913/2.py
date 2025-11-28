import numpy as np
import sys

N, M, L, U = map(int, input().split())
# N: カードの枚数, M: 山の数, L: 山の数字の下限, U: 山の数字の上限
# print(N, M, L, U)
# sys.stdout.flush()

rng = np.random.default_rng()
Al = rng.integers(U, size=(N))
Ail = [0] * N
print(*Al)
sys.stdout.flush()

Bl = list(map(int, input().split()))

yamaList = [0] * N

for _ in range(10):
    for i, Bi in enumerate(Bl):
        # print(Al)
        Aidx = np.argmin(np.abs(Al + yamaList[i] - Bi))
        # print(Aidx, Al[Aidx], Bi)
        if Al[Aidx] >= 0:
            Ail[Aidx] = i + 1
            yamaList[i] += Al[Aidx]
            Al[Aidx] = -1
        else:
            continue

print(*Ail)
sys.stdout.flush()  