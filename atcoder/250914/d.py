N, K = map(int, input().split())
# N組の団体, K席ある

t = 0

seki = []

A_list = [] # 到着時刻
B_list = [] # 食事の時間
C_list = [] # 人数

while True:
    print(seki)
    A, B, C = map(int, input().split())
    A_list.append(A) # 到着時刻
    B_list.append(B) # 食事の時間
    C_list.append(C) # 人数

    t = A_list[0]

    while True:
        seki.sort()
        if len(seki) == 0:
            break
        if t + seki[0] <= A_list[0]:
            dt = seki[0]
            t += dt
            seki = [x - dt for x in seki if x - dt > 0]
        else:
            break

    

    if A_list[0] <= t and len(seki) + C_list[0] < K:
        selected_A = A_list.pop(0)
        selected_B = B_list.pop(0)
        selected_C = C_list.pop(0)
        seki.extend([selected_B] * selected_C)