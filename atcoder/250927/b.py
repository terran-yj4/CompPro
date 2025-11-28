N = int(input())
A = list(map(int, input().split()))

if len(A) - A.count(-1) == len(set(A) - {-1}):
    print("Yes")
    nokori = [i for i in range(1, N + 1) if i not in A]
    for i in range(N):
        if A[i] == -1:
            A[i] = nokori.pop()
    print(*A)
else:
    print("No")
