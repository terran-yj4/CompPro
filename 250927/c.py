import numpy as np

N, Q = map(int, input().split())
A = list(map(int, input().split()))

A = np.array(A)
AA = np.concatenate([A, A])

top_idx = 0
sum_A = {}
S = np.zeros(2 * N + 1, dtype=int)
for i in range(2 * N):
    S[i + 1] = S[i] + AA[i]

for _ in range(Q):
    inp = input().split()
    
    if inp[0] == "1": # 1 c： A の先頭の要素を末尾に移動させる操作を c 回行う。
        c = int(inp[1])
        top_idx = (top_idx + c) % N

    else:   # 2 l r: l 番目から r 番目までの要素の和を出力。
        l, r = int(inp[1]), int(inp[2])
        print(S[top_idx + r] - S[top_idx + l - 1])