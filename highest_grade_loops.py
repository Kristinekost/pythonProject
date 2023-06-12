student_scores = input("Input a list of students scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max_num = 0
for i in student_scores:
    if i > max_num:
        max_num = i
print(max_num)
