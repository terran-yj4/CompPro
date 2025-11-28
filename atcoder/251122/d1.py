N, M = map(int, input().split())
A = list(map(int, input().split()))

max_keta = len(str(max(A)))
print(max_keta, max(A))

A = [i % M for i in A]

tens = [10 ** i for i in range(max_keta+1)]
print(tens)

Ns = [a % M for a in tens]
print(f"Ns: {Ns}")
print(A)

# mod_dict[桁数][余りの数]で個数        ここで桁数とは、2なら百の位に該当する数の1の位があるという意味。
mod_dict = {i: [0] * M for i in range(1, 10)}
print(mod_dict)

for a in A:
    for ten in tens:
        mod_dict[a * ten % M][len(str(ten))-1] += 1
        

print(mod_dict)





"""
4 7
2 8 16 183


2 11
2 42

22 : 2 * 10 + 2
(mod) 9 + 2






"""