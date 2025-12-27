N = int(input())
A = list(map(int, input().split()))

# print(N)
# print(A)

l = [[-1, 0]]

for i, v in enumerate(A):
    if l[-1][0] == v:
        l[-1][1] = (l[-1][1] + 1) % 4
        
    else:
        l.append([v, 1])
l.pop(0)

is_changed = True

while is_changed:
    is_changed = False
    print(l)
    for li in l:
        if li[1] >= 4:
            li[1] %= 4
            is_changed = True
        if li[1] == 0:
            l.remove(li)
            is_changed = True

    for i in range(len(l)-1):
        if l[i][0] == l[i+1][0]:
            is_changed = True
            l[i+1][1] += l[i][1]
            l[i][1] = 0

sum_cnt = 0

for li in l:
    sum_cnt += li[1]

print(sum_cnt)