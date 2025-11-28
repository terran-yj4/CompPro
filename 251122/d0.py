N, M = map(int, input().split())
A = input().split()

cnt = 0

for a1 in A:
    for a2 in A:
        if int("".join([a1, a2])) % M == 0:
            cnt += 1

print(cnt)