N, Q = map(int, input().split())

maxX = 0
dict = {i: 0 for i in range(1, N+1)}
n = 0
maxX = 0
cnt = 0
for _ in range(Q):
    # print(dict)
    n = 0
    cnt = 0
    X, Y = map(int, input().split())
    # print(f"X, Y = {X}, {Y}")
    if X <= maxX:
        print(0)
        # print()
        continue
    for k in list(dict.keys()):
        if k < X:
            n += dict.pop(k)
            
    # print(n, X, maxX)
    cnt =  n + X - maxX
    dict[Y] += cnt
    # print(dict)
    maxX = max(maxX, X)
    # print("maxX;", maxX)
    print(cnt)
    # print()
