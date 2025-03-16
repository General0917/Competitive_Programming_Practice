# 各桁の和を求める関数
def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total % 10

# メイン処理
if __name__ == "__main__":
    # 入力を受け取る
    bob_number, alice_number = map(int, input().split())

    # BobとAliceの各桁の和を計算
    bob_sum = sum_of_digits(bob_number)
    alice_sum = sum_of_digits(alice_number)

    # 結果を判定
    if bob_sum > alice_sum:
        print("Bob")
    elif bob_sum < alice_sum:
        print("Alice")
    else:
        print("Draw")
