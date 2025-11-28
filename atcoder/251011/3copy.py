from itertools import product

# input
N, M = map(int, input().split())

a = list(product('01', repeat=N))
a = a[:int(len(a)/2)]
print(a)

# input
l = []
for i in range(M):
    ui, vi = map(int, input().split())
    l.append((ui-1, vi-1))

cnts = {i: 0 for i in range(len(a))}

print(f"l: {l}")

for i, ai in enumerate(a):
    for li in l:
        if ai[li[0]] == ai[li[1]]:
            cnts[i] += 1

print(min(cnts.values()))
