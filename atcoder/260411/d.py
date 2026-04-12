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

"""未完成"""

class Node:
    def __init__(self, i, j, type: str):
        self.i = i
        self.j = j
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.type = type

    def next_nodes_hw(self, direction: str):
        next_nodes: set = {}
        if type == "#":     # このマスに立ち入ることはできない
            pass
        elif type == ".":   # このマスに自由に出入りすることができる
            next_nodes.add((self.i, self.j+1))
            next_nodes.add((self.i, self.j-1))
            next_nodes.add((self.i+1, self.j))
            next_nodes.add((self.i-1, self.j))
        elif type == "o":   # 直前の移動と同じ方向に移動しなければならない
            if direction == "r":
                next_nodes.add((self.i, self.j+1))
            elif direction == "l":
                next_nodes.add((self.i, self.j-1))
            elif direction == "u":
                next_nodes.add((self.i-1, self.j))
            else:
                next_nodes.add((self.i+1, self.j))
        elif type == "x":   # 直前の移動と同じ方向に移動することはできない
            next_nodes.add((self.i, self.j+1))
            next_nodes.add((self.i, self.j-1))
            next_nodes.add((self.i+1, self.j))
            next_nodes.add((self.i-1, self.j))
            if direction == "r":
                next_nodes.remove((self.i, self.j+1))
            elif direction == "l":
                next_nodes.remove((self.i, self.j-1))
            elif direction == "u":
                next_nodes.remove((self.i-1, self.j))
            else:
                next_nodes.remove((self.i+1, self.j))
        elif type == "S":   # このマスに自由に出入りすることができる
            next_nodes.add((self.i, self.j+1))
            next_nodes.add((self.i, self.j-1))
            next_nodes.add((self.i+1, self.j))
            next_nodes.add((self.i-1, self.j))

        if self.up:
            next_nodes.remove((self.i-1, self.j))
        if self.down:
            next_nodes.remove((self.i+1, self.j))
        if self.left:
            next_nodes.remove((self.i, self.j-1))
        if self.right:
            next_nodes.remove((self.i, self.j+1))
        
        for next_node in list(next_nodes):
            if self.i > next_node[0] and self.j == next_node[1]:
                self.up = True
            elif self.i < next_node[0] and self.j == next_node[1]:
                self.down = True
            elif self.i == next_node[0] and self.j > next_node[1]:
                self.left = True
            elif self.i == next_node[0] and self.j < next_node[1]:
                self.right = True
        
        return next_nodes

    def set_flag(self, cur_i, cur_j, next_i, next_j):
        if cur_i > next_i:
            self.up = True
        elif cur_i < next_i:
            self.down = True
        elif cur_j > next_j:
            self.left = True
        else:
            self.right = True



input_text = """3 5
.#...
.Sooo
..x.G"""

# H, W = MI()
H, W = 3, 5
# S = []
# for h in range(H):
#     S.append(list(input()))
S = [['.', '#', '.', '.', '.'], ['.', 'S', 'o', 'o', 'o'], ['.', '.', 'x', '.', 'G']]
print(S)


def dfs(h, w, direction: str):
    next_nodes = S[h][w].next_nodes_hw(direction)
    if len(next_nodes) == 0:
        return
    for next_node in next_nodes:
        dfs(next_node[0], next_node[1], direction)


dfs(0, 0, "r")

print(S[0][0].up, S[0][0].down, S[0][0].left, S[0][0].right)
print("未完成")