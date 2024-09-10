# 请补充你的代码
# 提示用户输入体重（公斤）
weight = float(input("请输入您的体重（公斤）："))

# 提示用户输入身高（米）
height = float(input("请输入您的身高（米）："))

# 计算BMI值
bmi = weight / (height ** 2)

# 输出BMI值，保留两位小数
print(f"您的BMI值为：{bmi:.2f}")

# 根据BMI值输出健康建议
if bmi < 18.5:
    print("体重过轻")
elif 18.5 <= bmi < 24.9:
    print("体重正常")
elif 25 <= bmi < 29.9:
    print("体重超重")
else:
    print("肥胖")
