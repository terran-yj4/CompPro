n,k = map(int,input().split())

def base10int(value, base) -> str:
    """8進数から9進数に変換できる関数"""
    if (int(value // base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

for j in range(k):
    tmp = list(base10int(int(str(n),8),9))
    # print(tmp)
    for i in range(len(tmp)):
        if tmp[i] == "8":
            tmp[i] = "5"
    n = "".join(tmp)

print(int("".join(tmp)))
