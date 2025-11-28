S, A, B, X = map(int, input().split())

c, r = X // (A + B), X % (A + B)
rr = min(r, A)

print(( c * S * A ) + rr * S)


"""
S A B X
7 3 2 11

11 = 5 * 2 + 1

21 * 2 + 7

------------------

S A B X
6 3 2 9

9 = 5 * 1 + 3 + 1


"""
