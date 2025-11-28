X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

sum = X
l = [False] * N

for _ in range(Q):
    n = int(input()) - 1
    if l[n]:
        sum -= W[n]
        l[n] = False
    else:
        sum += W[n]
        l[n] = True
    print(sum)
