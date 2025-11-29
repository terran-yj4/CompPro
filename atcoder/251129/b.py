N, M = map(int, input().split())

d = {i + 1: {"c": 0, "s": 0} for i in range(M)}

for _ in range(N):
    Ai, Bi = map(int, input().split())
    d[Ai]["c"] += 1
    d[Ai]["s"] += Bi

for i in range(M):
    print(d[i+1]["s"] / d[i+1]["c"])