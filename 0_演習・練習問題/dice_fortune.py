import random

# コマンドライン・ターミナルに表示する文章。
print("\n\tサイコロ占い！")
print("サイコロの数字によって、占いを教えます！")

# コマンドライン・ターミナルに入力した値を受け取って、playという変数に渡す。
play = input("\nサイコロを投げてみますか？ (y/n) ")

# playの値がyである限り、中のコードを繰り返し実行。
while play == 'y':
    # 1から6の間でランダムに数字を選択。
    roll = random.randint(1, 6)

    print("\nあなたが投げたサイコロの数字は... " + str(roll) + "！")

    print("\nあなたの占いは... ")

    # 数字がマッチしたら、その中のコードだけを実行。
    if   roll == 1:
        print("近いうちにあなたに不幸が訪れます。")
    elif roll == 2:
        print("今夜、あなたに不幸が訪れます。")
    elif roll == 3:
        print("明日、あなたに不幸が訪れます。")
    elif roll == 4:
        print("来週、あなたに不幸が訪れます。")
    elif roll == 5:
        print("来月、あなたに不幸が訪れます。")
    elif roll == 6:
        print("来年、あなたに不幸が訪れます。")

    play = input("\nまたサイコロを投げてみますか？ (y/n) ")