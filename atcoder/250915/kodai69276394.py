n,m,l,u = map(int,input().split())
a = []
for i in range(n):
    a.append(str(99800000000000+(i%m)*400000000000//50))
print(" ".join(a))

b = list(map(int,input().split()))

# print(" ".join(["0"]*n))
ans = []
m_list = list(range(1,m+1))
# print(m_list)
for i in range(n):
    ans.append(str(m_list[i%(m)]))
print(" ".join(ans))