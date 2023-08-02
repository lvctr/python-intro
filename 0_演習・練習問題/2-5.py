# 組み込み関数使えます！
def min_n(list):
    return min(list)

# 組み込み関数使わないのであれば：
def min_n(list):
    # 比較対象をリストの最初の値に初期化する。
    min = list[0]

    # リストを順番に見ていく。
    for n in list:
        # もし今現在見てるnがminより小さければ、minをそのnの値に変える。
        if n < min:
            min = n
    # 繰り返していくと、最終的にminが一番大きい値に変わる。

    # minを返す。
    return min