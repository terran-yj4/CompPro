N, M = map(int, input().split())
C = list(map(int, input().split())) # 鍵の強さ
R = list(map(int, input().split())) # 開錠能力

C.sort()
R.sort()

c_idx = 0

cnt = 0

for r in R:
    if c_idx == len(C):
        break

    if C[c_idx] <= r:
        c_idx += 1
        cnt += 1


print(cnt)