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

N, T = MI()
A = li()

d = dict()
# d[0] = 1
# 1: 開く, 2: 閉じる

for a in A:
    d[a] = 2

is_open = True
last_open = 0
sum_open = 0
is_debug = True


while True:
    if d.items():
        k = min(d.keys())
        v =  d.pop(k)
    else:
        break
    if k > T:
        break
    if v == 1 and not is_open:
        if is_debug: print(f"開く: t={k}")
        last_open = k
        is_open = True
    elif v == 2 and is_open:
        d[k+100] = 1
        if is_debug: print(f"閉める: t={k}")
        is_open = False
        sum_open += k - last_open
    if is_debug: print(f"is_open={is_open}, last_open={last_open}, d={k - last_open}, sum_open={sum_open}")
if is_open:
    sum_open += T - last_open

if is_debug: print(d)
print(sum_open)