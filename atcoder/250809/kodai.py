n,q = map(int,input().split())
a = list(map(int,input().split()))
b = []
cnt = 0
tmp = 0
ans = []
for i in range(q):
    b.append(int(input()))

dict_x = {}

x = 2
cnt_q = 0
while len(a) > 0:
    print(a)
    cnt_q += 1
    # print(a)
    if cnt_q > 1:
        cnt += tmp
    tmp = len(a)
    a = list(map(lambda x: x-1, a))
    a = list(filter(lambda x: x > 0, a))
    dict_x[cnt_q] = cnt + 1
    print(cnt_q,cnt+1,)
    ans.append(cnt + 1)
# print(ans)

for bi in b:
    print(dict_x.get(bi,-1))



for i in range(sum(a)):
    
