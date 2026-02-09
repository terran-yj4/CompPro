n, l, r = map(int, input().split())
p = list(map(int, input().split()))

max = -1
max_idx = -2

for i, v in enumerate(p):
  if l <= v <= r :
    if v > max:
      max = v
      max_idx = i

print(max_idx+1)