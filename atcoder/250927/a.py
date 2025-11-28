
N = int(input())
print(sum([i ** 3 * (-1) ** i for i in range(1, N + 1)]))