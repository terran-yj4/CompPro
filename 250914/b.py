N = int(input())
L = list(map(int, input().split())) # 0の時鍵は開いている、1の時閉じている

if L.count(1) == 0 or L.count(1) == 1:
    print(0)
else:
    fidx = L.index(1)
    L.reverse()
    ridx = N - 1 - L.index(1)
    print(ridx - fidx)

