N, M = map(int, input().split())

G=[[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

sd = [""] + list(input())

# print(G)

def a(n):
    # print(f"n: {n}")
    route = {}
    def dfs(p, cnt, reached=[]):
        if sd[p] == "S":
            if p not in route.keys():
                route[p] = cnt
            route[p] = min(route[p], cnt)
        for pp in set(G[p]) - set(reached):
            dfs(pp, cnt+1, reached + [p])

    dfs(n, 0)
    mins = []
    # print(f"route: {route}")
    sorted_item = sorted(route.items(), key=lambda item: item[1])
    # print(sorted_item)
    print(sorted_item[0][1] + sorted_item[1][1])

for i, item in enumerate(sd):
    if item == "D":
        a(i)