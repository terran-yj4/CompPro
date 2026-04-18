import os,sys,random,threading
from random import (
    randint,            # randint(a,b)          [a,b]の範囲からランダムに数を選択
    choice,             # choice(seq)           seqからランダムに要素を選択 (seqはlist, str, tuple型)
    shuffle             # shuffle(x)            可変シーケンスxの要素をシャッフル xを書き換え 成功時の返り値はNone
)
from copy import (
    deepcopy            # x.deepcopy()          オリジナルとコピー先で別のオブジェクトとして扱われる 
)
from collections import (
    Counter,            # Counter([1, 2, 2])    数を数えるときに便利 Counter({2: 2, 1: 1})を生成
    defaultdict,        # defaultdict(int)      キー生成のいらないdict 初期値0で自動で初期化してくれる defaultdict(lambda: defaultdict(int))
    deque               # q = deque()           キュー
)
from itertools import ( # イテレータを生成する関数が入っている
    accumulate,         # accumulate(l)         累積和の時使える            for a in accumulate(l): print(a)
    combinations,       # combinations(seq, k)  seqからk個選ぶ組み合わせ    for i in combinations(l, 2): print(i)
    permutations,       # permutations(seq, k)  seqからk個並べる並び方      for i in permutations(l, 2): print(i)
    product,            # product(seq1, seq2)   直積を求める                product([1, 2], [3, 4]) -> [(1, 3), (1, 4), (2, 3), (2, 4)]
    combinations_with_replacement
)

l = [1, 2, 4, 8]
l2 = [1, 2, 4, 8]
l3 = [1, 2, 4, 8]

p = product(l, l2, l3)
print(p)
for pp in p:
    print(pp)