n = int(input())

A = [pow(3, i) for i in range(12)]
B = [sum(A[:i])for i in range(1, len(A))]

A.sort(reverse=True)
B.sort(reverse=True)
B.append(0)

digit = ""

for i, a in enumerate(A):
    # print(a+B[i], a-B[i], i, a)
    if a-B[i] <= abs(n) <= a+B[i]:
        digit += "1" if n >= 0 else "2"
        n += a if n < 0 else -a
    else:
        digit += "0"

print(int(digit))