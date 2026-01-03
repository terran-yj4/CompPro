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
py = lambda :print("Yes")
pn = lambda :print("No")

from time import time

s1 = time()

def a(l):
    return sum([pow(i, 2) for i in l])

n = ii()

l = list(map(int, list(str(n))))
# print(l)
history = [n]

while True:
    n = a(l)
    if n == 1:
        py()
        break
    if n in history:
        pn()
        break
    history.append(n)
    l = list(map(int, list(str(n))))
    # print(l)