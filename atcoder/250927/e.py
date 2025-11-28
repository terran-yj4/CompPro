from decimal import Decimal
import math
import numpy as np

T, M = map(int, input().split())

for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    res = 1

    for c in C:
        res *= math.factorial(c)
        N -= 1

    a = math.factorial(sum(C)) // np.prod(list(map(math.factorial, C)))
    print(a % M)