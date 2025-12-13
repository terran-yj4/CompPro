N = int(input())

table = [[0 for _ in range(N)] for _ in range(N)]
r = 0
c = int((N - 1) / 2)
k = 1
table[0][c] = k

for _ in range(pow(N, 2) - 1):
    k += 1
    if table[(r-1)%N][(c+1)%N] == 0:
        r = (r-1)%N
        c = (c+1)%N
    else:
        r = (r+1)%N
        c = c%N
    table[r][c] = k

for l in table:
    print(" ".join(map(str, l)))
