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
import numpy as np
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

T = ii()

for _ in range(T):
    N = ii()
    R = np.array(li(), dtype=np.int64)
    sum_c = 0
    # 値の小さい順にランキング（インデックスの並び）
    order = np.argsort(R)

    for o in order:
        slf = R[o]
        # 隣を取得
        neighbors = []
        if o - 1 >= 0:
            neighbors.append(R[o - 1])
        if o + 1 < N:
            neighbors.append(R[o + 1])
        if not neighbors:
            continue

        max_neighbor = max(neighbors)
        # 自分が隣より小さかったら、自分を 隣-1 にして増量を sum_c に追加
        if slf < max_neighbor:
            new_val = max_neighbor - 1
            add = new_val - slf
            R[o] = new_val
            sum_c += add

    print(sum_c)



"""
1
5
5 2 1 3 4

"""