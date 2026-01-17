is_debug = False

N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=False)    # 小さい順
Al = A[:K]
Alr = [0]

for al in Al:
    Alr.append(Alr[-1]+al)

if is_debug:
    print("--debug--")
    print("Al", Al)
    print(Alr)
    print("---------")

cnt = 0

for i, v in enumerate(Alr):
    if v >= X:
        cnt = i
        break


if cnt == 0:
    print(-11)  # 6
else:
    # N-Kは適当に選んだうち最悪全ての水を選んだ場合の数
    print(N-K+cnt)  # 6