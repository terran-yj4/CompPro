H, W = map(int, input().split())

table = []

for _ in range(H):
    table.append(list(input()))

cnt = 0

def is_ok(i, j):
    cnt_b = 0
    if i > 0 and table[i-1][j] == "#":
        cnt_b += 1
    if i < H-1 and table[i+1][j] == "#":
        cnt_b += 1
    if j > 0 and table[i][j-1] == "#":
        cnt_b += 1
    if j < W-1 and table[i][j+1] == "#":
        cnt_b += 1
    return cnt_b in [4, 2]


flag = True

for i in range(H):
    for j in range(W):
        if table[i][j] == "#":
            if not is_ok(i, j):
                flag = False
                break
    else:
        continue
    break
print("Yes" if flag else "No")
