import numpy as np

N = int(input())
A = list(map(int, input().split()))

a = sorted(A)
print(A.index(a[-2])+1)

A.sort()