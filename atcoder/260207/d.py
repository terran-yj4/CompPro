N = int(input())
A = list(map(int, input().split()))

d = dict()
for i in range(max(A) + 1):
    d[i] = 0
for a in A:
    d[a] += 1

n = 0
cum = 0

for k in sorted(d.keys(), reverse=True):
    cum += d[k]
    n += cum * (10 ** (k - 1))

print(n)