A = str(input())
B = str(input())

# Aの文字列の末尾を取得
A_last = A[-1]

# B文字列の先頭を取得
B_first = B[0]

# Bの文字列の末尾を取得
B_last = B[-1]

# Aの文字列の末尾がBの文字列の先頭と同じかつ、Bの文字列の末尾が「n」の場合、「NG」、そうでない場合は、「OK」と出力する
if A_last == B_first and B_last != 'n':
    print('OK')
else:
    print('NG')