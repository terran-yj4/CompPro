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

n = ii()

def make_div(n):
    ld , ud = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            ld.append(i)
            if i != n // i:
                ud.append(n//i)
        i += 1
    return ld + ud[::-1]

def r2(n: int) -> int:
    divs = make_div(n)
    c1 = sum(1 for d in divs if d % 4 == 1)
    c3 = sum(1 for d in divs if d % 4 == 3)
    return 4 * (c1 - c3)

l = []

for num in range(1, n+1):
    cnt = r2(num)
    root = int(sqrt(num))
    # if root * root == num:  # 平方数の場合
    #     cnt -=4
    # h_root = int(sqrt(num/2))
    # if h_root * h_root == num/2:
    #     cnt -= 2
    # if cnt == 8:
    #     l.append(str(num))
    print(num, cnt)

print(len(l))
print(" ".join(l))

