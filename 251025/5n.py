# ...existing code...
from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

sd = [""] + list(input().strip())

def solve_from_D(start):
    dist = [-1] * (N + 1)
    dq = deque([start])
    dist[start] = 0
    while dq:
        v = dq.popleft()
        for to in G[v]:
            if dist[to] == -1:
                dist[to] = dist[v] + 1
                dq.append(to)
    s_dists = [dist[i] for i in range(1, N + 1) if sd[i] == "S" and dist[i] != -1]
    if len(s_dists) < 2:
        print(-1)
    else:
        s_dists.sort()
        print(s_dists[0] + s_dists[1])

for i in range(1, N + 1):
    if sd[i] == "D":
        solve_from_D(i)
# ...existing code...