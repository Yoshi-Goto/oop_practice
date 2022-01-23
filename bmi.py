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
        self.height = height_m
        self.weight = weight_kg
        self.value = self.weight / pow(self.height, 2)


yg = BMI(height_m=1.7, weight_kg=65)
print(yg.height)
print(yg.weight)
print(yg.value)
