S = input()

a = S[0]
if S.count(a) == 1:
    print(a)
else:
    print(S.replace(a, ""))