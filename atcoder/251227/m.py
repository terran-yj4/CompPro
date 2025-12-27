from time import sleep
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
print(l)

is_changed = True

new_l = []

while True:
    print(l)
    sleep(1)
    last_num = -1
    cnt = 0
    for i, v in enumerate(l):
        if v[0] == last_num:
            cnt += 1
            v[1] = 0
        else:
            if i != 0:
                l[i-1] = [last_num, cnt]
            last_num = v[0]
            cnt = 1
    l[-1] = [last_num, cnt]


    for i in range(len(l)-1, 0, -1):
        if l[i][1] == 0:
            l.pop(i)
