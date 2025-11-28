from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

pow10 = [1] * 11
for i in range(1, 11):
    pow10[i] = pow10[i-1] * 10 % M

# 各長さごとにAj % Mの個数をカウント
count = [defaultdict(int) for _ in range(11)]
for a in A:
    l = len(str(a))
    count[l][a % M] += 1

ans = 0
for a in A:
    for l in range(1, 11):
        rem = (a * pow10[l]) % M
        need = (-rem) % M
        ans += count[l][need]
    # Ai, Ajが同じ時にf(Ai, Aj)がMの倍数かどうかを除外
    if (a * pow10[len(str(a))] + a) % M == 0:
        ans -= 1

print(ans)