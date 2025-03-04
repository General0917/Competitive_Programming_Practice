# 入力データのサイズ
n = int(input())
stones = []

# stones 配列の入力
for _ in range(n):
    stones.append(list(map(int, input().split())))

# 動的に目標のピラミッドパターン生成
target = [[0] * n for _ in range(n)]
center = n // 2

for i in range(center + 1):
    for j in range(i, n - i):
        target[i][j] = i + 1
        target[j][i] = i + 1
        target[n - 1 - i][j] = i + 1
        target[j][n - 1 - i] = i + 1

# 結果を計算
total_stones_to_remove = 0
for i in range(n):
    for j in range(n):
        stones_to_remove = stones[i][j] - target[i][j]
        if stones_to_remove > 0:
            total_stones_to_remove += stones_to_remove

# 結果を出力
print(total_stones_to_remove)
