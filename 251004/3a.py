from sortedcontainers import SortedSet, SortedList, SortedDict

N, Q = input().split()

max = 0
dict = SortedDict()

for _ in range(int(Q)):
    X, Y = map(int, input().split())
    if X <= max:    # Xの最大値以下なら無視
        print(0)
        continue
    num = X - max   # 2
    max = X
    dels = []
    for k, v in dict.items():
        if k <= X:
            num += v
            dels.append(k)
        else:
            break
            
    for i in dels:
        dict.pop(i)
    
    if Y not in dict:
        dict[Y] = num
    else:
        dict[Y] += num
    print(num)
