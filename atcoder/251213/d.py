H, W = map(int, input().split())
table = []

"""
. : 空きマス
# : 障害物マス
英小文字（a - z）: ワープマス
"""

access = dict()
abc_dict = {c: [] for c in list("abcdefghijklmnopqrstuvwxyz")}

for _ in range(H):
    table.append(list(input()))

for i in range(H):
    access[i] = dict()
    for j in range(W):
        access[i][j] = set()
        if table[i][j] == "#":
            continue
        elif table[i][j] != ".":
            abc_dict[table[i][j]].append((i, j))
        if i - 1 >= 0 and table[i - 1][j] != "#":
            access[i][j].add((i - 1, j))
        if i + 1 < H and table[i + 1][j] != "#":
            access[i][j].add((i + 1, j))
        if j - 1 >= 0 and table[i][j - 1] != "#":
            access[i][j].add((i, j - 1))
        if j + 1 < W and table[i][j + 1] != "#":
            access[i][j].add((i, j + 1))

for k, v in abc_dict.items():
    for vv in v:
        access[vv[0]][vv[1]].update((set(v)-{vv}))

print(table)
print(access)
print(abc_dict)

mincost = float("inf")


def h(p: tuple, c: int):
    global mincost
    if mincost < c:
        return
    if p == (H, W):
        mincost = min(mincost, c)
        return
    for cp in access[p[0]][p[1]]:
        h(cp, c+1)

h((0, 0), 0)

print(mincost)