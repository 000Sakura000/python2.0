#7 ��������д����
import math
radius = 6371 * 1000
# 1. ��������������������ʽS = 4��R2��
surface_area = 4*math.pi*radius*radius
print(f'��������Ϊ{surface_area:.2f}ƽ����')

# 2. �����������������ʽ��V = 4��R3/3��
volume =4*math.pi*radius*radius*radius/3
print(f'�������Ϊ{volume:.2f}������')

# 3. ������������ܳ���Բ�ܳ���ʽ��L = 2��R��
circumference = 2*math.pi*radius
print(f'�������ܳ�Ϊ{circumference:.2f}��')
# 4.�������������֮��Ŀ�϶��С
new_radius = (circumference+1)/(2*math.pi)-radius
print(f'��϶��СΪ{new_radius:.2f}��')

# 5.�ж������Ƿ���Դӿ�϶�����
if new_radius>=0.1:
    print("������Դӿ�϶�����")
    
else:
    print("�����޷�ͨ����϶")
    