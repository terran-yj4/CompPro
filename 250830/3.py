N = int(input())
S = input()

def suretsu(n):
    return int(1/2 * n * (1 + n))

splited_A = S.split('A')

list_A = []

for i, s in enumerate(S):
    if s == 'A': list_A.append(i)

# print(list_A)

list_A_mirai_1 = [i for i in range(0, N * 2, 2)]

# print(list_A_mirai_1)

sum_AB = 0
sum_BA = 0

for a, b in zip(list_A, list_A_mirai_1):
    # print(a, b, abs(a - b))
    sum_AB += abs(a - b)
    sum_BA += abs(a - (b + 1))
print(min(sum_AB, sum_BA))
