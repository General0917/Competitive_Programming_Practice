# 入力を受け取る
line = int(input())

# エレベーターの初期値
elevator = 1
total_distance = 0

# エレベーターの移動回数
for _ in range(line):
    floor = int(input())

    # エレベーターの移動
    total_distance += abs(floor - elevator)

    # エレベーターの現在位置を更新
    elevator = floor

print(total_distance)
