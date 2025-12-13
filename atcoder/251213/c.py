N, M = map(int, input().split())

put_tiles = {}  # 各行(key)の何列目にタイルの右上を置いたかを保存する辞書

for i in range(M):
    # print(put_tiles)
    R, C = map(int, input().split())
    R, C = R-1, C-1
    for i in range(-1, 2):
        target_r = R + i
        if target_r < 0 or target_r >= N:
            continue
        # print(put_tiles[target_r] & set([C - 1, C, C + 1]))
        if target_r not in put_tiles: # そもそも存在しない
            continue
        if put_tiles[target_r] & set([C - 1, C, C + 1]):
            break
        # if R + i in put_tiles.keys() and not (put_tiles[R + 1] & set([C - 1, C, C + 1])):
        #         break
        # else:
        #     print("被りなし")
    else:
        # 被らない時追加
        # if R not in put_tiles.keys():
        #     put_tiles[R] = {C}
        # else:
        if R not in put_tiles:
            put_tiles[R] = set()
        put_tiles[R].add(C)
        # print("add", R, C)
    # print("01:", put_tiles[R])
    # print("02:", set([C-1, C, C+1]))
    # print("O3:", put_tiles[R] & set([C-1, C, C+1]))

    # if all(not put_tiles[r] & (set([C-1, C, C+1])) for r in range(max(0, R - 1), min(N-1, R + 1))):
    #     put_tiles[R].add(C)
    #     print(f"addしたよ{R, C}")


print(sum(len(v) for v in put_tiles.values()))