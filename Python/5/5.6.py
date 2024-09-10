# 补充你的代码
# 接收用户输入的对齐符号和占位宽度
align_symbol = input()
width = int(input())

# 定义圆周率的不同精度
pi1 = '3.14'
pi2 = '3.1415'
pi3 = '3.1415926'

# 使用f-string输出指定格式的字符串，控制对齐和宽度
print(f'圆周率值为：{pi1:{align_symbol}{width}}')
print(f'圆周率值为：{pi2:{align_symbol}{width}}')
print(f'圆周率值为：{pi3:{align_symbol}{width}}')
 