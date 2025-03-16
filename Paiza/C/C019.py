# 入力を受け取る
Q = int(input())
numbers = []

for _ in range(Q):
    numbers.append(int(input()))

for value in numbers:
    sum_of_divisors = 0
    for i in range(1, value):
        if value % i == 0:
            sum_of_divisors += i

    if value == sum_of_divisors:
        print("perfect")
    elif abs(value - sum_of_divisors) == 1:
        print("nearly")
    else:
        print("neither")
