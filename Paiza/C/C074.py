# 入力を受け取る
H, W, X = map(int, input().split())

# テキストを結合する
text = ""
for _ in range(H):
    text += input()

# 全ての文字列を特定の長さごとに分割して出力
length = len(text)
for i in range(0, length, X):
    if i + X < length:
        print(text[i:i + X])
    else:
        print(text[i:])
