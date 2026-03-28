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

N = ii()

bl = [pow(2, i) for i in range(30)]
# print(bl)
keta_bl = [-1, 3, 6, 9, 13, 16, 19, 23, 26, 29] # idx=ketaの数字まで使う


def kettei(kazu: str, nokori: int, bls: list):
    res = []
    for bl in bls:
        if len(str(bl)) > nokori:
            continue
        else:
            if nokori-len(str(bl)) == 0:
                # print("0!!!", kazu, bl)
                res.append(kazu+str(bl))
            else:
                # print("0以外!!", kazu, bl)
                r = kettei(kazu=kazu+str(bl), nokori=nokori-len(str(bl)), bls=bls)
                res.extend(r)
    return res


bls = []
for i in range(10):
    # if i <= 3: print(f"i={i}, keta: 0-{keta_bl[i]+1}, bls={sorted(bl[0:keta_bl[i]+1])}")
    r = kettei(kazu="", nokori=i, bls=sorted(bl[0:keta_bl[i]+1]))
    bls.extend(r)


bls = sorted(set(map(int, bls)))

print(bls[N-1])
