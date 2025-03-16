# CLIから整数を入力する
num = int(input())

point = 0
for _ in range(num):
    # スペースで区切られた入力を取得
    line = input().split()
    day = int(line[0])
    amount = int(line[1])

    # 日付に応じたポイントの計算
    if '5' in str(day):
        point += amount * 0.05
    elif '3' in str(day):
        point += amount * 0.03
    else:
        point += amount * 0.01

print(int(point))
