Q = int(input())

n = 0   # 今入れている()
l = []
f_idx = -1

for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        l.append(1 if q[1] == "(" else -1)
        if n == 0 and l[-1] == -1 and f_idx == -1:
            f_idx = len(l) - 1  # ダメポイント
        n += l[-1]
        print("Yes" if n == 0 and f_idx == -1 else "No")
    else:
        n -= l.pop()
        if len(l) == f_idx:
            f_idx = -1
        print("Yes" if n == 0 and f_idx == -1 else "No")

    # print(n, l, f_idx)