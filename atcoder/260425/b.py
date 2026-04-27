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

# .→しろ, #→黒

H, W = MI()
table = []
cnt = 0

for _ in range(H):
    table.append(list(input()))

def a(i, j, k, l):
    s = ""
    for h in range(i, i+k+1):
        s += "".join(table[h][j:j+l+1])
    return s

for i in range(H):
    for j in range(W):
        # i, jが右上
        for k in range(H-i):
            for l in range(W-j):
                s = a(i, j, k, l)
                # print(i, j, i+k, j+l)
                # print("s: ", s)
                if s == s[::-1]:
                    cnt += 1

print(cnt)