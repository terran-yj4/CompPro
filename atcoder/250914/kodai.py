x,c = map(int,input().split())
if x - 1000 < c:
    print(0)
    exit()
    
for i in range(x,0,-1000):
    if i+i*c//1000 < x:
        print(i)
        break
