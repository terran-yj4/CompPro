from math import lcm
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

# N, X, Y = 3, 6, 8
# A = [11, 10, 13]

# N, X, Y = 2, 3, 4
# A = [3, 5]
max_A = max(A)

Y_list = [Y * i for i in range(max_A+1)]
X_list = [X * i for i in range(max_A)]

print(Y_list, X_list)