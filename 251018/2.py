from sortedcontainers import SortedDict
N, K = map(int, input().split())    # 1≤K≤N≤100
S = input() # 英小文字からなる長さ N の文字列

words = SortedDict()

for i in range(N - K + 1):
    txt = S[i:i+K]
    if txt in words.keys():
        words[txt] += 1
    else:
        words[txt] = 1

max_txt = []
max_count = 0

for k, v in words.items():
    if v > max_count:
        max_txt = [k]
        max_count = v
    elif v == max_count:
        max_txt.append(k)

print(max_count)
print(*max_txt)