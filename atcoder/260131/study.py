l = [1, 2, 3]
l.pop(0)    # O(N)

from collections import deque
q = deque([1, 2, 3])
q.popleft()  # O(1)