# ������εĳ�
length = float(input())

# ������εĿ�
width = float(input())

# �������
area = length * width

# ��������������������������������������
if area.is_integer():
    print(int(area))
else:
    print(area)
