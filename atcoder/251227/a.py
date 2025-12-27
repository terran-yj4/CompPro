D, F = map(int, input().split())

d = F

while True:
    d += 7
    if d > D:
        print(d-D)
        break