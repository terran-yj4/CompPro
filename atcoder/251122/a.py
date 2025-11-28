x, y, z = map(int, input().split())
if (y > x):
    print("No")
else:
    if y * z <= x:
        a = (x - y * z) / (z - 1)
        print("Yes" if a % 1 == 0 else "No")
    else:
        print("No")