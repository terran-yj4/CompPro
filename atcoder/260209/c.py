n, k = map(int, input().split())
d = list(map(int, input().split()))

d = sorted(d)
sum = 0

for i in range(n-k):
    sum += d[i]

print(sum)