from collections import deque
l = [1, 2, 3]
l.pop(0)    # O(N)

q = deque(l)
q.popleft() # (1)