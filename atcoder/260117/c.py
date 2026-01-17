N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=False)    # 小さいじゅん

Al = A[:K]
Alr = [0]

for al in Al:
    Alr.append(Alr[-1]+al)

# print(Al)
# print(Alr)

# print("----")
cnt = 0

for i, v in enumerate(Alr):
    if v >= X:
        cnt = i
        break

if cnt == 0:
    print(-1)
else:
    print(N-K+cnt)