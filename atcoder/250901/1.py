import numpy as np

N, K = input().split()

K = int(K)

for _ in range(K):
    base8 = int(N, 8)
    N = str(np.base_repr(base8, 9)).replace('8', '5')


print(int(N))