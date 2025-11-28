# AHC 形式（N M L U を受け取り、A を出力→B を受信→X を出力）
# 方針：
#   1) まず各山に L を 1 枚ずつ（M 枚）。
#   2) その後、K 層ぶんの重みカードを用意（各層 g*2^k を M 枚ずつ）。
#      M*(1+K) <= N となる最大の K を使う。
#      g は (2^K - 1) * g >= (U-L) を満たすように天井で決める。
#   3) B を受け取ったら d_j = B_j - L を g で丸め、
#      t_j = clamp(round(d_j/g), 0, 2^K-1) を K ビットに展開して配る。
#      各層は「各山 0/1 個まで」なので、在庫超過は起きない。
#
# 制約想定: N=500, M=50 など。numpy不要・O(MK)。

import sys

def read_needed_ints(n):
    vals = []
    while len(vals) < n:
        line = sys.stdin.readline()
        if not line:
            break
        vals.extend(map(int, line.strip().split()))
    return vals[:n]

def main():
    N, M, L, U = map(int, sys.stdin.readline().split())

    # 使える層数 K（基準 M 枚 + 層ごとに M 枚、合計が N 以下）
    K = max(0, N // M - 1)

    # カバーすべき幅
    width = max(0, U - L)

    # g の決定： (2^K - 1) * g >= width となる最小の g
    if K > 0:
        denom = (1 << K) - 1
        g = (width + denom - 1) // denom
        if g <= 0:
            g = 1
    else:
        g = 1  # K=0 のときは実質未使用

    # A を構成
    A = []
    # まず各山に L を 1 枚ずつ
    for _ in range(M):
        A.append(L)

    # 重みカード（各層ごとに M 枚）
    weights = []
    for k in range(K):
        w = g * (1 << k)
        if w < 1:
            w = 1
        if w > U:
            # 値は U 以下である必要があるので抑える（通常は超えないはず）
            w = U
        weights.append(w)
        for _ in range(M):
            A.append(w)

    # 余りがあればダミー（1）で埋める（全部捨てるので OK）
    while len(A) < N:
        A.append(1)

    # 出力1：A
    print(*A)
    sys.stdout.flush()

    # 入力：B（M 個、昇順）
    B = read_needed_ints(M)

    # 各山のターゲット値との差分を g 単位で丸め、ビット展開
    # t_j in [0, 2^K - 1]
    if K > 0:
        t = []
        cap = (1 << K) - 1
        for bj in B:
            d = bj - L
            # 四捨五入（最近接の g の倍数に）
            tj = int(round(d / g))
            if tj < 0:
                tj = 0
            elif tj > cap:
                tj = cap
            t.append(tj)
    else:
        t = [0] * M

    # 出力2：X（各カードがどの山に行くか。0 は捨てる）
    X = [0] * N

    # まず基準 L カード（先頭 M 枚）を各山に 1 枚ずつ
    for j in range(M):
        X[j] = j + 1

    # 各層の重みカードをビットに応じて配る
    # インデックス管理：層 k のブロック開始は base = M + k*M
    for k in range(K):
        base = M + k * M
        for j in range(M):
            if ((t[j] >> k) & 1) == 1:
                X[base + j] = j + 1  # j 番目の山へ
            # 0 のときは捨て札のまま(=0)

    # 余りカードは全て 0（既定値）で捨てる

    print(*X)
    sys.stdout.flush()

if __name__ == "__main__":
    main()
