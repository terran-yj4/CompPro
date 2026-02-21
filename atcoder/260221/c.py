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

T = ii()
# T = 1

for t in range(T):
    N, D = MI() # N日間営業, D日以上経過した卵は処分
    A = li()    # A_i個の卵を仕入れる。
    B = li()    # B_i個の卵を使用、仕入れた順に。
    # N, D = 3, 1
    # A = [7, 2, 3]
    # B = [1, 3, 2]
    q = deque([], D+1)
    for i, b in enumerate(B):
        q.append(A[i])
        while b:
            lf = q.popleft()
            if lf > b:
                q.appendleft(lf-b)
                break
            elif lf == b:
                break
            else:   # lf < b
                b -= lf

    q.append(0)
    print(sum(q))
