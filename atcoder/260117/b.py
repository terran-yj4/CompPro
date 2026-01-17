N, M = map(int, input().split())
S = set(input())
T = set(input())
Q = int(input())

only_s = S - T
only_t = T - S
# print(only_s, only_t)

for _ in range(Q):
    s_flag = False  # 髙橋である可能性
    t_flag = False  # 青木
    w = input()
    s_flag = any([s in w for s in only_s])
    t_flag = any([t in w for t in only_t])

    if s_flag:
        print("Takahashi")
    elif t_flag:
        print("Aoki")
    else:
        print("Unknown")
