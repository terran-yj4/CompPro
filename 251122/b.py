N = int(input())
A = list(map(int, input().split()))

for i, a in enumerate(A):
    done = False
    for j in range(i-1, -1, -1):
        if A[j] > a:
            print(j+1)
            done = True
            break
    if not done: print(-1)

