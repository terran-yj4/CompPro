# N, Q = map(int, input().split())    # N: フルーツの種類数, Q: クエリの数
N, Q = 4, 1
# A = list(map(int, input().split())) # フルーツの個数のlist
A = [4, 1, 8, 4]

b = 2

dict_A = {0: 0}

for i in A:
    if i not in dict_A:
        dict_A[i] = 0
    dict_A[i] += 1

print(dict_A)   # {1: 1, 4: 2, 8: 1}
# 残っている数のdictに変換？
# 4: (4-1) * (4-2) + (1-0) * (4-0) = 3 * 2 + 1 * 4 = 10

print(dict_A.items())

usingList = [a for a in dict_A.items() if a[0] < b]
usingList.sort()
if usingList[-1][0]+1 != b:
    usingList.append((b-1, 0))


sum = 0
delcnt = 0
print(usingList)
for i in range(len(usingList)):
    if i == 0:
        sum += (usingList[i][0] - 0) * (N - delcnt)
        print(f"sum: {sum}")
    else:
        delcnt += usingList[i-1][1]
        sum += (usingList[i][0] - usingList[i-1][0]) * (N - delcnt)
        print(f"sum: {sum}")

print(f"final sum: {sum + 1}")



for _ in range(Q):
    pass

"""

4 1 8 4
1 4 4 8
1           2       3       4       5   6   7   8
| 4 1 8 4 | 4 8 4 | 4 8 4 | 4 8 4 | 8 | 8 | 8 | 8 
4.            3       3       3     1   1   1   1 

>> 4: (1 - 0) * (4 - 0) + (3 - 2 + 1) * (4 - 1)  + 1
    = 1 * 4 + 2 * 3 + 1
    = 4 + 6 + 1
    = 11

1: 1    -> 4
2: 0    -> 3
3: 0    -> 3
4: 2    -> 3
5: 0    -> 1
6: 0    -> 1
7: 0    -> 1
8: 1    -> 1
9: 0    -> 0




"""
