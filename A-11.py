# A-11: BMIアプリ

weight_input = float(input("体重を入力してください(kg): "))
height_input = float(input("身長を入力してください(m): "))

bmi = round(weight_input / (height_input * height_input), 2)

print(f"あなたのBMIは {bmi} です")

# 小数点以下2桁にする。
# 　BMI＝ 体重kg ÷ (身長m)2
# 　適正体重＝ (身長m)2
