#4
tuition_per_credit = eval(input('������ÿѧ��ѧ�ѽ�'))
living_expenses = eval(input('��������ÿ��������ѣ�'))

total_credits = 17 # ��ѧ��
total_tuition = total_credits * tuition_per_credit
total_cost = living_expenses * 5 + total_tuition
student_loan = total_cost * 0.6

print(f'��ѧ�����ܹ�����{student_loan:.2f}Ԫ')