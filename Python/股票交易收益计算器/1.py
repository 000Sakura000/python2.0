# �벹����Ĵ���
# ��ʾ�û������Ʊ������۸�ÿ�ɣ�
buy_price = float(input("�������Ʊ������۸�ÿ�ɣ���"))

# ��ʾ�û������Ʊ�������۸�ÿ�ɣ�
sell_price = float(input("�������Ʊ�������۸�ÿ�ɣ���"))

# ��ʾ�û�������еĹ�Ʊ����
quantity = int(input("��������еĹ�Ʊ������"))

# ����������
total_profit = (sell_price - buy_price) * quantity

# ����ʽ��������棬������λС��
print(f"������Ϊ��{total_profit:.2f} Ԫ")
