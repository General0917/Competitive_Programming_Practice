import re

# ユーザーIDから番号部分を抽出する関数
def extract_number(user_id):
    number_part = re.sub(r'[^0-9]', '', user_id)
    return int(number_part)

# メイン処理
if __name__ == "__main__":
    # ユーザー数を読み込む
    n = int(input())

    # ユーザーIDを格納するリストを作成
    user_ids = [input().strip() for _ in range(n)]

    # ユーザーIDを並べ替える
    user_ids.sort(key=lambda user_id: extract_number(user_id))

    # 並べ替えたユーザーIDを出力
    for user_id in user_ids:
        print(user_id)
