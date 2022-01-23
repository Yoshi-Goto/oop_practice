"""
データ型の宣言：Username
    属性：文字型
        実際のユーザー名
    ルール：
        ユーザー名は４文字以上２０文字以内である
    できること：
        ユーザー名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        # nameのチェック
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}はルール違反です。')
        self.name = name

    def battle_name(self):
        return self.name.upper()


bob = UserName(name='Bob Smith')
print(bob.name)
print(bob.battle_name())
