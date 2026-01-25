from calendar import c
import enum
from numpy import argsort, sort

import os,sys,random,threading
from random import randint,choice,shuffle
#randint(a,b)[a,b]の範囲からランダムに数を選択
#choice(seq)seqはリスト、タプルまたは文字列で、seqからランダムに要素を選択
#shuffle(x)可変シーケンスxの要素をシャッフル
from copy import deepcopy
from collections import Counter,defaultdict,deque
from itertools import accumulate,combinations, count,permutations
#accumulate(a)シーケンスaから累積イテレータを生成、通常はリスト化して前に[0]を置いて累積和に使用
#combinations(a,k)シーケンスaからk個を選ぶ 組み合わせイテレータ
#permutations(a,k)シーケンスaからk個を選ぶ 順列イテレータ
from math import ceil,floor,sqrt,pi,factorial,gcd,log,log10,log2,inf, atan2, degrees
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

# def getRD(x, y):
#     r = sqrt(x**2+y**2)
#     rad = atan2(y, x)
#     degree = degrees(rad)
#     # print(r, degree)
#     return r, degree

def getRD2(idx, x, y):
    r = sqrt(x**2+y**2)
    rad = atan2(y, x)
    # degree = degrees(rad)
    # print(r, degree)
    return idx, r, rad


rd: list = []
rd_dict: dict = defaultdict(list)
counter = Counter()
idx_deg: dict = defaultdict()
deg_rd_idx: dict = defaultdict(int)

N, Q = MI()

for i in range(1, N+1):
    X, Y = MI()
    # rd_dict[i] = getRD2(i, X, Y)
    # rd.append(rd_dict[i])  # 極座標変換して配列に入れる
    idx, r, deg = getRD2(i, X, Y)
    rd_dict[deg].append((idx, r, deg))
    idx_deg[i] = deg
    counter[deg] += 1

rd_list = sorted(rd_dict.items(), key= lambda x: x[0])
# print(rd_list)

for i, v in enumerate(rd_list):
    deg_rd_idx[v[0]] = i

for i in range(len(rd_list)):
    rd_list[i] = len(rd_list[i][1])

rd_list2 = rd_list + rd_list
rd_list2_rr = [0]

for v in rd_list2:
    rd_list2_rr.append(rd_list2_rr[-1] + v)

# print(rd_list2)
# print(rd_list2_rr)
# print(idx_deg.items())
# print(counter)
# print(deg_rd_idx.items())

rd_len = len(rd_list)

for q in range(Q):
    A, B = MI()

    deg_A = idx_deg.get(A)
    deg_B = idx_deg.get(B)
    idx_A = deg_rd_idx.get(deg_A) + 1
    idx_B = deg_rd_idx.get(deg_B)
    
    # print(idx_A, idx_B)

    if idx_B == idx_A:
        print(N)
    else:
        if idx_B > idx_A:
            idx_A += rd_len
        print(rd_list2_rr[idx_A] - rd_list2_rr[idx_B])
