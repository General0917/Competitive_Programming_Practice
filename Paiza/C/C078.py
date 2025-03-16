# 入力を受け取る
N, c1, c2 = map(int, input().split())  # 日数、買値の基準、売値の基準
prices = [int(input()) for _ in range(N)]  # 日ごとの株価をリストで取得

stocks = 0  # 持ち株数
cash = 0  # 現金

# 株価の変動に応じた処理
for i in range(N):
    if prices[i] <= c1:
        # 株価がc1以下の場合は1株購入
        stocks += 1
        cash -= prices[i]
    elif prices[i] >= c2:
        # 株価がc2以上の場合はすべて売却
        cash += stocks * prices[i]
        stocks = 0

# N日目に残りの株をすべて売却
cash += stocks * prices[-1]
stocks = 0

# 損益を出力
print(cash)
