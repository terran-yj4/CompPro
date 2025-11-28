N, M = map(int, input().split())

dict_uv = {i: [] for i in range(1, N+1)}

for i in range(M):
    ui, vi = map(int, input().split())
    dict_uv[ui].append(vi)

for k, v in dict_uv.items():
    dict_uv[k].sort()

# print(dict_uv)

cnt = 0

for k, v in dict_uv.items():
    # print("k, v: ", k, v)
    if len(v) != 0:
        for i in range(len(v)):
            for vi in v[i:]:
                if vi in dict_uv[v[i]]:
                    dict_uv[v[i]].remove(vi)
                    cnt += 1

print(cnt)