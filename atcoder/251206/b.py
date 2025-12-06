N = int(input())
A = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        # print(f"i, j: {i}, {j}")
        s = sum_A = sum(A[i:j+1])
        is_not_prime = True
        for k in range(i, j+1):
            if s % A[k] == 0:
                is_not_prime = False
                break
        if is_not_prime:
            # print(i, j, s)
            cnt += 1
print(cnt)