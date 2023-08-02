import math

# listを受け取る
def calculate_sum(list):
    # 和を入れる変数を初期化する。
    # 何も足されていない状態なので、0に初期化。
    sum = 0

    # リストを順番に見ていく。
    for n in list:
        # sum (和が入っている変数) に、
        #   n (順番に見ていってるリストの中に入ってる数字)
        #   を足していく。
        sum += n
    
    # 最終的に得た和を返す。
    return sum