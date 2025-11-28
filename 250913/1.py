import numpy as np
import sys

N, M, L, U = map(int, input().split())
# print(N, M, L, U)
sys.stdout.flush()

rng = np.random.default_rng()
Al = rng.integers(U, size=(N))
Ail = [0] * N
print(*Al)
sys.stdout.flush()

Bl = list(map(int, input().split()))

yamaList = [0] * N
endsList = [False] * N

while endsList.count(True) < N:
    # print(endsList.count(True))
    sys.stdout.flush()
    for i, Bi in enumerate(Bl):
        if endsList[i]:
            continue
        valid_idx = np.where(Al >= 0)[0]
        if len(valid_idx) == 0:
            endsList[i] = True
            continue
        tmp = np.abs(Al[valid_idx] + yamaList[i] - Bi)
        idx = valid_idx[np.argmin(tmp)]
        # print(idx, Al[idx], Bi, yamaList[i])
        sys.stdout.flush()
        if Al[idx] >= 0:
            if abs(yamaList[i] + Al[idx] - Bi) < abs(yamaList[i] - Bi):
                yamaList[i] += Al[idx]
                Al[idx] = -1
                Ail[idx] = i + 1
                endsList[i] = True
            else:
                endsList[i] = True
                continue
        else:
            endsList[i] = True
            continue

print(*Ail)
print()
sys.stdout.flush()