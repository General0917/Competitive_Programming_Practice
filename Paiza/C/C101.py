# 入力を受け取る
X = int(input())

count = 0
# 0から364までループ
for i in range(365):  # rangeは0から364まで
    if str(X) in str(i):  # 数字iにXが含まれるかをチェック
        count += 1

# 結果を出力
print(count)
