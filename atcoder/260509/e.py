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

## 動かん

N, M = MI()
d = defaultdict(lambda: defaultdict(list))
for m in range(M):
    a, b = MI()
    d["s"][a].append(b)
    d["t"][b].append(a)

print(d)

Q = ii()

for q in range(Q):
    S, T = MI()
    d["s"][S].sort(reverse=True)
    d["t"][T].sort()
    s = [si for si in d["s"][S] if si <= T][0:2]
    t = [ti for ti in d["t"][T] if ti >= S][0:2]
    print(f"s: {s}, t: {t}")

    if s and t:
        l = []
        for ss in s:
            l.append((S,ss))
        if s[0] == T:
            t.popleft()
        if s[1] == T:
            t.popleft()
        for tt in t:
            l.append((tt,T))
        
        print(l)
