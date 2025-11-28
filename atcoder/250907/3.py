T = int(input())    # 回数

for _ in range(T):
    n_A, n_B, n_C = map(int, input().split())

    ave = (n_A + n_B + n_C) // 3
    if n_A > ave:
        n_A, n_B = ave, n_B + (n_A - ave)
    if n_C > ave:
        n_C, n_B = ave, n_B + (n_C - ave)
    
    print(min(n_B, n_A, n_C))
    