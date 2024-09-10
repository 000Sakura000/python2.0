#3
python = 3
math = 4
english = 4
pe = 2
military = 2
philosophy = 2

credits = python + math + english + pe + military + philosophy
tuition_per_credit = int(input(""))

total_tuition = credits * tuition_per_credit

print(f"你本学期选修了{credits}个学分。")
print(f"你应缴纳的学费为{total_tuition}元。")