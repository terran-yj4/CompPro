import numpy as np

n,m,l,u = map(int,input().split())
# N: カードの枚数, M: 山の数, L: 山の数字の下限, U: 山の数字の上限

a = []  # 最初のやつ 50
for i in range(50):
    a.append(997400000000000+(i%m)*400000000000//5)

rng = np.random.default_rng()  # シード値（任意）
Al = rng.integers(100000000000, 1000000000000, size=450)

result = list(map(str, a)) + [str(x) for x in Al.tolist()]
print(" ".join(result))

b = list(map(int,input().split()))

ans = [x for x in range(1, 51)] + [0] * 450

for i, bi in enumerate(b):
    Aidx = np.argmin(np.abs(bi - a[i] - Al))
    if Al[Aidx] >= 0:
        ans[Aidx + 50] = i + 1
        Al[Aidx] = -1
    else:
        continue

print(" ".join(list(map(str, ans))))