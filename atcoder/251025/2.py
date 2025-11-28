N, M = map(int, input().split())

A = list(map(int, input().split()))

sum_A = sum(A)

c = sum_A - M

if c in A:
    print("Yes")
else:
    print("No")
