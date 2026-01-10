T = int(input())

for i in range(T):
    N, W = map(int, input().split())
    C = list(map(int, input().split()))
    # print(f"{i+1}回目のテストケース" , N, W)
    q_dict = {i: 0 for i in range(2*W)}             # O(N)
    for i, v in enumerate(C):                   # O(N)
        q_dict[i % (2*W)] += v
    
    rl_items = list(q_dict.values())*2                # O(N)?
    rl = [0]
    for rl_item in rl_items:
        rl.append(rl[-1] + rl_item)
    # print(rl)
    # [2, 20, 20, 2, 2, 20, 20, 2]
    # Wの数だけ

    sums = []
    for i in range(2*W):
        sums.append(rl[i+W] - rl[i])
        
    # print(f"sums: {sums}")
    print(min(sums))
