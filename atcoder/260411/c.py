import os,sys,random,threading
from random import randint,choice,shuffle
#randint(a,b)[a,b]の範囲からランダムに数を選択
#choice(seq)seqはリスト、タプルまたは文字列で、seqからランダムに要素を選択
#shuffle(x)可変シーケンスxの要素をシャッフル
from copy import deepcopy
from collections import Counter,defaultdict,deque
from itertools import accumulate,combinations,permutations,product,combinations_with_replacement
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

N = ii()
l = li()

elements = (1, -1)

# 重複ありの順列（直積）を生成
combinations = list(product(elements, repeat=len(l)))

max_cnt = 0

# 結果を表示
for comb in combinations:
    cnt = 0
    m = 0
    is_plus = True
    for i in range(len(l)):
        m += comb[i] * l[i]
        if m < 0:
            if is_plus:
                cnt += 1
            is_plus = False
        elif m >= 0:
            if not is_plus:
                cnt += 1
            is_plus = True
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
