import math
import numpy as np

T = int(input())


def f(x, y):
    return int(str(x) + y)

def get_prime_count(c, d):
    cnt = 0
    min_d = c
    max_d = c + d
    min_keta = len(str(min_d))
    max_keta = len(str(max_d))
    for i in range(min_keta, max_keta + 1):
        if i == min_keta:
            a = f(c, str(min_d))
            b = f(c, "9" * i)
        elif i == max_keta:
            a = f(c, "1" * i)
            b = f(c, str(max_d))
        else:
            a = f(c, "1" + "0" * (i - 1))
            b = f(c, "9" * i)
        
        r_a = np.ceil(np.sqrt(a))
        r_b = np.trunc(np.sqrt(b))
        # print(np.sqrt(a), np.sqrt(b), r_a, r_b, r_b - r_a + 1)
        cnt += r_b - r_a + 1
    return cnt

for _ in range(T):
    C, D = map(int, input().split())
    print(get_prime_count(C, D))