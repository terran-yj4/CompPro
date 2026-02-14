import os,sys,random,threading
from random import randint,choice,shuffle
#randint(a,b)[a,b]の範囲からランダムに数を選択
#choice(seq)seqはリスト、タプルまたは文字列で、seqからランダムに要素を選択
#shuffle(x)可変シーケンスxの要素をシャッフル
from copy import deepcopy
from collections import Counter,defaultdict,deque
from itertools import accumulate,combinations,permutations
#accumulate(a)シーケンスaから累積イテレータを生成、通常はリスト化して前に[0]を置いて累積和に使用
#combinations(a,k)シーケンスaからk個を選ぶ 組み合わせイテレータ
#permutations(a,k)シーケンスaからk個を選ぶ 順列イテレータ
from math import ceil,floor,sqrt,pi,factorial,gcd,log,log10,log2,inf
#ceil切り上げ、floor切り捨て、sqrt平方根、factorial階乗
input = lambda: sys.stdin.readline().rstrip("\r\n")
MI = lambda :map(int,input().split())

ls = lambda :list(input().split())                      # 文字列リスト
li = lambda :list(MI())                                 # 整数リスト
ii = lambda :int(input())                                    # 整数
inf = 1<<60
pY = lambda :print("YES")
pN = lambda :print("NO")
py = lambda :print("Yes")
pn = lambda :print("No")

########################################################

n = 10**100
n = 10
# n = 31
idx = 0
s = 0
l = []

while n > 0:
    n, r = divmod(n, 2) # nを2で割った商と余りを取得
    # print(f"n: {n} r: {r} idx: {idx} s: {s}")
    if r == 1:
        s += 2**idx
        l.append(idx)
    idx += 1

# print(s)
# print(l)


N = ii()
a = li()

cur = [0] + [a[i] for i in range(N)]
# O(N)
result = cur
# O(N)
print(result)

result = {n+1: n+1 for n in range(N)}
last_cur = cur

for i in range(1, 332):
    new_cur = cur
    for k, v in enumerate(cur):
        new_cur[k] = cur[v]
    if i in l:
        for k in range(1, N + 1):
            result[k] = new_cur[result[k]]
    last_cur = new_cur

print(*list(result.values()))