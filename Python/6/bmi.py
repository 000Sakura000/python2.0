# �벹����Ĵ���
# ��ʾ�û��������أ����
weight = float(input("�������������أ������"))

# ��ʾ�û�������ߣ��ף�
height = float(input("������������ߣ��ף���"))

# ����BMIֵ
bmi = weight / (height ** 2)

# ���BMIֵ��������λС��
print(f"����BMIֵΪ��{bmi:.2f}")

# ����BMIֵ�����������
if bmi < 18.5:
    print("���ع���")
elif 18.5 <= bmi < 24.9:
    print("��������")
elif 25 <= bmi < 29.9:
    print("���س���")
else:
    print("����")
