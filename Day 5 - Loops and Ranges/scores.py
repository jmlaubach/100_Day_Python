# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

maximum = student_scores[0]
for score in range(0, len(student_scores)):
    if student_scores[score]>maximum:
        maximum = student_scores[score]

maximum_str = str(maximum)

print(f"The highest score in the class is: {maximum_str}")
