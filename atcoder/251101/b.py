N, M = map(int, input().split())

table = []
result = []

for _ in range(N):
    table.append(input())

for i in range(N-M+1):
    for j in range(N-M+1):
        a = []
        # ここから
        for k in range(M):
            a.append(table[i+k][j:j+M])
        # print("-".join(a))
        result.append("-".join(a))

print(len(set(result)))