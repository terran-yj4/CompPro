N = int(input())
W, H, B = [], [], []

for _ in range(N):
    w, h, b = map(int, input().split())
    W.append(w)
    H.append(h)
    B.append(b)

ruisekiwa_happiness, ruisekiwa_W, ruisekiwa_H, ruisekiwa_B = [0], [0], [0], [0]

total = 0

for i in range(N):
    total += max(H[i], B[i])
    ruisekiwa_happiness.append(total)
    ruisekiwa_W.append(ruisekiwa_W[-1] + W[i])
    ruisekiwa_H.append(ruisekiwa_H[-1] + H[i])
    ruisekiwa_B.append(ruisekiwa_B[-1] + B[i])

# print(ruisekiwa_happiness)
# print(ruisekiwa_W)
# print(ruisekiwa_H)
# print(ruisekiwa_B)

################################################

# 2分探索
best_happiness = 0

# 今後最大値を更新できる -> True, できない -> False
def check_best(level, current_happiness):
    return best_happiness < current_happiness + ruisekiwa_happiness[-1] - ruisekiwa_happiness[level]
# ロボットが完成できる -> True, できない -> False
def check_complete(level, sum_head_w, sum_body_w):
    return sum_head_w <= sum_body_w + (ruisekiwa_W[-1] - ruisekiwa_W[level])

# 探索
def a(level, current_happiness, sum_head_w, sum_body_w):
    global best_happiness
    if level == N:
        if current_happiness > best_happiness and sum_head_w <= sum_body_w:
            # print(f"更新しました。{best_happiness} -> {current_happiness}, {sum_head_w}, {sum_body_w}")
            best_happiness = current_happiness
        return
    
    if not check_best(level=level, current_happiness=current_happiness):
        return
    if not check_complete(level=level, sum_head_w=sum_head_w, sum_body_w=sum_body_w):
        return

    # level番目のパーツを頭にセットした場合
    a(level=level+1, current_happiness=current_happiness + H[level], sum_head_w=sum_head_w + W[level], sum_body_w=sum_body_w)
    # level番目のパーツを体にセットした場合
    a(level=level+1, current_happiness=current_happiness + B[level], sum_head_w=sum_head_w, sum_body_w=sum_body_w + W[level])

a(0, 0, 0, 0)

# print(W, H, B)
# print(ruisekiwa_H, ruisekiwa_B)

print(best_happiness)