import collections
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
MI = lambda :map(int,input().split())
li = lambda :list(MI())                                 # 整数リスト

N, T = MI()
A = li()

# open_list = []
# close_list = []
open_queue = collections.deque()
close_queue = collections.deque()


for a in A:
    close_queue.append(a)

is_open = True
last_open = 0
sum_open = 0
is_debug = False

t = 0
while open_queue or close_queue:
    v = 0
    if not open_queue:
        t = close_queue.popleft()
        v = 2
    elif not close_queue:
        t = open_queue.popleft()
        v = 1
    elif open_queue[0] < close_queue[0]:
        t = open_queue.popleft()
        v = 1
    else:
        t = close_queue.popleft()
        v = 2
    
    if v == 1 and not is_open:
        if is_debug: print(t, last_open, sum_open)
        last_open = t
        is_open = True
    elif v == 2:
        if is_debug: print(t, last_open, sum_open)
        if is_open:
            open_queue.append(t+100)
            sum_open += t - last_open
            is_open = False

if is_open:
    if is_debug: print("最後")
    sum_open += max(0, T - last_open)
print(sum_open)