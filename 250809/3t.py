N, Q = map(int, input().split())    # N: フルーツの種類数, Q: クエリの数
A = list(map(int, input().split())) # フルーツの個数のlist

max_A = max(A)

for _ in range(Q):
    b = int(input())

    if b > max_A:
        print(-1)
        continue

    dict_A = {0: 0}

    for i in A:
        if i not in dict_A:
            dict_A[i] = 0
        dict_A[i] += 1

    usingList = [a for a in dict_A.items() if a[0] < b]
    usingList.sort()
    if usingList[-1][0]+1 != b:
        usingList.append((b-1, 0))

    sum = 0
    delcnt = 0
    for i in range(len(usingList)):
        if i == 0:
            sum += (usingList[i][0] - 0) * (N - delcnt)
        else:
            delcnt += usingList[i-1][1]
            sum += (usingList[i][0] - usingList[i-1][0]) * (N - delcnt)

    print(f"{sum + 1}")