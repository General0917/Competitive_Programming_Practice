rain = 0

a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] == 1:
        rain += 1

if rain >= 5:
    print("yes")
else:
    print("no")
