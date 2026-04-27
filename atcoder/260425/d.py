from operator import is_
import os,sys,random,threading
from random import randint,choice,shuffle
#randint(a,b)[a,b]の範囲からランダムに数を選択
#choice(seq)seqはリスト、タプルまたは文字列で、seqからランダムに要素を選択
#shuffle(x)可変シーケンスxの要素をシャッフル
from copy import deepcopy
from collections import Counter,defaultdict,deque
from itertools import accumulate,combinations,permutations,product,combinations_with_replacement
#accumulate(l) 累積和に使用 for v in accumulate(l): print(v)
#combinations(seq,k) シーケンスseqからk個を選ぶ 組み合わせイテレータ
#permutations(seq,k) シーケンスseqからk個を選ぶ 順列イテレータ
#product(seq,repeat=k) シーケンスseqからk個を選ぶ 直積イテレータ
#combinations_with_replacement(seq,k) シーケンスseqからk個を選ぶ 重複組み合わせイテレータ
from math import ceil,floor,sqrt,pi,factorial,gcd,log,log10,log2,inf
#ceil(x) xを切り上げ floor(x) xを切り捨て factorial(x) xの階乗 gcd(x,y) 最大公約数
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

N, Q = MI()
CP_list = []
for q in range(Q):
    C, P = MI()
    CP_list.append((C, P))
# print(N, Q, CP_list)

is_parent = [True] * (N + 1)
next_child = [0] * (N + 1)
d = defaultdict(int)

for cp in CP_list[::-1]:
    C, P = cp
    if not is_parent[C]: # もしCが親じゃなかったらスルー
        continue
    else:
        next_child[P] = C
        is_parent[C] = False

# print(is_parent, next_child)

ans = []

for n in range(1, N+1):
    if not is_parent[n]:
        ans.append(0)
        continue
    cnt = 0
    p = n
    while p != 0:
        cnt += 1
        p = next_child[p]
    ans.append(cnt)

print(*ans)