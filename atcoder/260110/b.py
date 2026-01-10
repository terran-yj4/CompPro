N = int(input())
T = list(map(int, input().split()))
sortedT = sorted(T)
# print(T, sortedT)
a = []
for i in range(3):
    # print(i, sortedT[i])
    a.append(str(T.index(sortedT[i])+1))

print(" ".join(a))