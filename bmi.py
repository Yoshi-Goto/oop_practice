"""
class *:
    関連する属性:
      - 身長(m)
      - 体重(kg)
      - BMIという値そのもの
    ルール:
      - BMIは22が適正 10以上40以下の範囲 <=常識的な範囲
      - 表示する時は小数点第2位まで
        - ex: 23.689 => 23.69
        - ex: 23.681 => 23.68
    できること:
      - BMIの計算
"""


class BMI:
    def __init__(self, height_m, weight_kg):
        self.value = weight_kg / pow(height_m, 2)
        if not (10 <= self.value <= 40):
            raise ValueError(f'BMI血が規定値を外れています。！！！{self.value}')

    def __str__(self):
        return f"{self.value:.2f}"


yg = BMI(height_m=1.7, weight_kg=65)
print(yg)
