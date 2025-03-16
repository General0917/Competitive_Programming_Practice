# CLIから整数を入力する
input_line = input().split()

N = int(input_line[0])
M = int(input_line[1])

for i in range(1, N + 1):
    line = input().split()
    test_point = int(line[0])
    number_of_absences = int(line[1])

    score = test_point - (number_of_absences * 5)

    if score < 0:
        score = 0

    if score >= M:
        print(i)
