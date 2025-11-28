n = int(input())

l = []

for _ in range(n):
    l.append(input())

a = input().split()

if l[int(a[0])-1] == a[1]:
    print("Yes")
else:
    print("No")