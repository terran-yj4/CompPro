N, M, K = map(int, input().split())
H = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

# print(H)
# print(B)

cnt = 0
hi = 0
bi = 0

while bi < M:
    # print(hi, bi)
    if H[hi] > B[bi]:
        bi += 1
        continue
    else:
        # print(f"bingo: {hi}, {bi}")
        cnt += 1
        hi += 1
        bi += 1
        if cnt >= K:
            break
# print(H)
# print(B)
print("Yes" if cnt >= K else "No")