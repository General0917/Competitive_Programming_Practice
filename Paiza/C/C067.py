# 入力を受け取る
number_of_digits, number = map(int, input().split())

# 各桁の指定位置を格納するリストを作成
positions = []
for _ in range(number_of_digits):
    positions.append(int(input()))

# 2進数に変換して文字列として取得
binary_string = bin(number)[2:]  # bin()を使用して2進数を取得し、"0b"を除去
length = len(binary_string)

# 各位置のビット値を出力
for position in positions:
    if position <= length:
        print(binary_string[length - position])
    else:
        print(0)  # 桁数より大きな場合は0を出力
