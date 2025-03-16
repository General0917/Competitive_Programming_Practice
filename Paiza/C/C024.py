# 入力を受け取る
t = int(input())
a = [0, 0]

for _ in range(t):
    # コマンドを分割して取得
    arrays = input().split()
    cmd = arrays[0]

    if cmd == "SET":
        j = int(arrays[1])
        k = int(arrays[2])
        a[j - 1] = k
    elif cmd == "ADD":
        l = int(arrays[1])
        a[1] = a[0] + l
    elif cmd == "SUB":
        m = int(arrays[1])
        a[1] = a[0] - m

print(a[0], a[1])
