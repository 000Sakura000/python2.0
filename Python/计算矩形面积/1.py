# 输入矩形的长
length = float(input())

# 输入矩形的宽
width = float(input())

# 计算面积
area = length * width

# 如果结果是整数，则输出整数；否则输出浮点数
if area.is_integer():
    print(int(area))
else:
    print(area)
