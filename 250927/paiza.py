"""ノードクラス"""
class Node:
    def __init__(self, cost):
        self.is_start = True
        self.is_start = False
        self.is_goal = False
        if cost == "S":
            self.is_start = True
            self.cost = 0
            self.min_cost = None
        elif cost == "G":
            self.is_goal = True
            self.cost = 0
            self.min_cost = None
        else:
            self.cost = int(cost)
            self.min_cost = 100000
    
    def set_min_sum_cost(self, min_cost: int):
        self.min_cost = min_cost



H, W = map(int, input().split())
cells = []
for _ in range(H):
    cells.append([Node(i) for i in list(input())])

start = None
goal = None
stack = []

for i in range(H):
    for j in range(W):
        if cells[i][j].is_start:
            start = (i, j)
        if cells[i][j].is_goal:
            goal = (i, j)

def dfs(i, j, sum_cost):
    if i < 0 or i >= H or j < 0 or j >= W:
        return
    cell = cells[i][j]
    if cell.is_start and sum_cost != 0:
        return
    if cell.is_goal:
        if cell.min_cost is None or cell.min_cost > sum_cost:
            cell.set_min_sum_cost(sum_cost)
        return
    if cell.min_cost is not None and cell.min_cost <= sum_cost + cell.cost:
        return
    cell.set_min_sum_cost(sum_cost + cell.cost)
    dfs(i+1, j, sum_cost + cell.cost)
    dfs(i-1, j, sum_cost + cell.cost)
    dfs(i, j+1, sum_cost + cell.cost)
    dfs(i, j-1, sum_cost + cell.cost)

dfs(start[0], start[1], 0)

print(cells[goal[0]][goal[1]].min_cost)