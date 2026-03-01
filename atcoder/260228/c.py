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

S = input()
T = input()

s_len = len(S)
t_len = len(T)

s_idx = 0
t_idx = 0
a_cnt = 0

cant = False

while True:
    if t_idx >= t_len or s_idx >= s_len:
        break
    if T[t_idx] == S[s_idx]:
        s_idx += 1
        t_idx += 1
    elif T[t_idx] != S[s_idx]:
        if S[s_idx] == "A":
            a_cnt += 1
            s_idx += 1
        elif T[t_idx] == "A":
            a_cnt += 1
            t_idx += 1
        else:
            cant = True
            break

if t_idx >= t_len:
    if S[s_idx:].count("A") == s_len - s_idx:
        a_cnt += S[s_idx:].count("A")
    else:
        cant = True
elif s_idx >= s_len:
    if T[t_idx:].count("A") == t_len - t_idx:
        a_cnt += T[t_idx:].count("A")
    else:
        cant = True

if cant:
    print(-1)
else:
    print(a_cnt)