n, k = map(int, input().split())
a = list(map(int, input().split()))

if k not in a:
    print(-1)
else:
    index = a.index(k)
    print(index + 1)