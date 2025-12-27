N, M = map(int, input().split())

S = input()
T = input()


# N , M = 4, 2
# S = "2025"
# T = "91"

cnts = []

for s_idx in range(len(S) - len(T) + 1):
    # print(f"Sのスタート: {s_idx}")
    cnt = 0
    for t_idx in range(len(T)):
        # print(f"s: {s_idx + t_idx}, t: {t_idx}")
        # print(f"{(int(S[s_idx + t_idx]) - int(T[t_idx])) % 10}")
        cnt += (int(S[s_idx + t_idx]) - int(T[t_idx])) % 10
    cnts.append(cnt)

print(min(cnts))
        

1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 1 
1 1 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2