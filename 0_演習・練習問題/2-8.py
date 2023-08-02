def len_list(list):
    # まず長さを0に初期化。
    length = 0

    # リストの中身を順番に見ていく。
    for i in list:
        # アイテムがあれば、lengthを足していく。
        length += 1

    # 最終的に得られた長さを返す。
    return length