# 組み込み関数使えます！
def max_n(list):
    return max(list)

# 組み込み関数使わないのであれば：
def max_n(list):
    # 比較対象をリストの最初の値に初期化する。
    max = list[0]

    # リストを順番に見ていく。
    for n in list:
        # もし今現在見てるnがmaxより大きければ、maxをそのnの値に変える。
        if n > max:
            max = n
    # 繰り返していくと、最終的にmaxが一番大きい値に変わる。

    # maxを返す。
    return max