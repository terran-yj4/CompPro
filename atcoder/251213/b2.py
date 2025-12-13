N = 5

t = [0] * N
t[3][2][1] = 1

for l in t:
    print(" ".join(map(str, l)))