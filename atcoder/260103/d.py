"""

このコードは正解していません。

"""

import os,sys,threading
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
py = lambda :print("YES")
pn = lambda :print("NO")

N = ii()
A = li()

d = dict()

for i, v in enumerate(A):
    if v not in d.keys():
        d[v] = {i}
    else:
        d[v].add(i)
print(d)

for j_num, idxs in d.items():
    if j_num % 5 != 0: continue
    i_num, k_num = j_num/5*7, j_num/5*3,
    i_idxs = d[i_num]
    k_idxs = d[k_num]
    i_all_cnt = len(i_idxs)
    k_all_cnt = len(i_idxs)


    for idx in idxs:
        i_lg_idxs = len([i_idx for i_idx in i_idxs if i_idx > idx])
        l_
