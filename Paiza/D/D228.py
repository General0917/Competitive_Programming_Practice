S, T = map(int, input().split())
H, M = map(int, input().split())

current = H * 60 + M
sunset = S * 60 + T

if current >= 0 and current <= sunset:
    print("Yes")
else:
    print("No")