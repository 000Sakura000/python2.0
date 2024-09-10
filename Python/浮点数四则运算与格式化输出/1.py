# 输入第一个浮点数
num1 = float(input())

# 输入第二个浮点数
num2 = float(input())

# 计算加、减、乘、除
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

# 输出结果，保留小数点后3位数字
print(f"{num1} + {num2} = {add_result:.3f}")
print(f"{num1} - {num2} = {sub_result:.3f}")
print(f"{num1} * {num2} = {mul_result:.3f}")
print(f"{num1} / {num2} = {div_result:.3f}")