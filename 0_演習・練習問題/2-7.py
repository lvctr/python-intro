# 二次方程式の解 = (-b±√(b²-4ac))/(2a)

# 複素数を扱えるmathをインポート
import cmath

# aとbとcを受け取る
def quad(a, b, c):
    # 判別式 b²-4ac の計算
    d    = (b ** 2) - (4 * a * c)

    # ±なので、解は2つあります。両方計算。
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    # 2つの解を一気に返すことが可能。
    # タプル（不変なリスト）として返されます。
    return (sol1, sol2)