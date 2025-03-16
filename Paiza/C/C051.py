# 入力の解析
def parse_input(input_str):
    number_strings = input_str.split(" ")
    numbers = [int(num) for num in number_strings]
    return numbers

# 最大和を計算
def calculate_max_sum(numbers):
    max_sum = 0
    for i in range(4):
        for j in range(4):
            if i != j:
                num1 = numbers[i] * 10 + numbers[j]
                for k in range(4):
                    for l in range(4):
                        if k != l and k != i and k != j and l != i and l != j:
                            num2 = numbers[k] * 10 + numbers[l]
                            max_sum = max(max_sum, num1 + num2)
    return max_sum

# メイン処理
if __name__ == "__main__":
    input_str = input()
    numbers = parse_input(input_str)
    max_sum = calculate_max_sum(numbers)
    print(max_sum)
