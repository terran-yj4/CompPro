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

# できてない


# M, A, B = MI()
M, A, B = 4, 1 ,2

x = 1
y = 5

s_1 = y
s_2 = x
print(s_2)
print(s_1)

for _ in range(1):
    s_1, s_2 = A * s_1 + B * s_2, s_1
    print(s_1, s_2)
    s11, s21 = s_1, s_2
    s_1, s_2 = A * s_1 + B * s_2, s_1
    s12, s22 = s_1, s_2
    print(s_1, s_2)
    s_1, s_2 = A * s_1 + B * s_2, s_1
    s13, s23 = s_1, s_2
    print(s_1, s_2)
    s_1, s_2 = A * s_1 + B * s_2, s_1
    print(s_1, s_2)
    s_1, s_2 = A * s_1 + B * s_2, s_1
    print(s_1, s_2)
    s_1, s_2 = A * s_1 + B * s_2, s_1
    
    print(s21 % M == 0 or s22 % M == 0 or s23 % M == 0, "FならOK")
    print(s11, s21, s12, s22, s13, s23)
    print(s11%M, s21%M, s12%M, s22%M, s13%M, s23%M)
    # print(str(s11 % M)[-2:] == str(s21 % M)[-2:], str(s21 % M)[-2:] == str(s12 % M)[-2:])