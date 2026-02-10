N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))




for n in range(N):
    for m in range(M):
        if A[n] + B[m] == K:
            print(n+1, m+1)
            exit()

print(-1)