"""
编写程序，用户入自己的姓名，输出以下界面后，再在下一行输出“欢迎您，***同学！”
|++++++++++++++++++++++|
|                      |
|   Welcome to WHUT    |
|                      |
|++++++++++++++++++++++|
"""

my_name = input()  # 输入学生的姓名                             
########### Begin ############
# 输出以上界面
print('|++++++++++++++++++++++|')
print('|                      |')
print('|   Welcome to WHUT    |')
print('|                      |')
print('|++++++++++++++++++++++|')

# 输出“欢迎您，***同学！”
print(f'欢迎您，{my_name}同学！')

########### End ############