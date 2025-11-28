import sys

N, ti, tj = map(int, sys.stdin.readline().split())
grid = [list(sys.stdin.readline().strip()) for _ in range(N)]

# 最初のターン開始
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break

    pi, pj = map(int, line.split())
    n = int(sys.stdin.readline())
    confirmed = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # 冒険者が花に到達したら終了
    if (pi, pj) == (ti, tj):
        break

    print(0)
    sys.stdout.flush()
