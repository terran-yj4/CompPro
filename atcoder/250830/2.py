X, Y = map(int, input().split())

an_1 = X
an_2 = Y

def f(an_1, an_2):
    return an_2, int(str(an_1 + an_2)[::-1])

for i in range(8):
    an_1, an_2 = f(an_1, an_2)
print(an_2)