N, R = map(int, input().split())        # ドアの個数, 髙橋君の始めの部屋番号
L = list(map(int, input().split()))     # 0の時鍵は開いている、1の時閉じている


if N / 2 < R:  # 先左に行く
    L.reverse()
    R = N - R
l_l = L[:R]
l_r = L[R:]

sum = 0

if l_l.count(0) >= 1:
    zero_first_idx = 0
    if l_l.count(0) >= 1:
        zero_first_idx = l_l.index(0)
    sum += l_l[zero_first_idx:].count(1) * 2    # 開けて閉める数
    sum += l_l[zero_first_idx:].count(0)        # 閉める数

if l_r.count(0) >= 1:
    zero_last_idx = len(l_r)
    if l_r.count(0) >= 1:
        l_r.reverse()
        zero_last_idx = len(l_r) - l_r.index(0)
        l_r.reverse()
    sum += l_r[:zero_last_idx].count(1) * 2
    sum += l_r[:zero_last_idx].count(0)
print(sum)







""" 0の時鍵は開いている、1の時閉じている

8 2
0 1 0 0 1 0 1 1
0 1 X 3 4 5 6 7 8

左 3


6 0
1 1 1 1 1 1

6 5   
 0 1 1 1 1 1
0 1 2 3 4 X 6 7 8


"""