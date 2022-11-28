# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)): 
  student_heights[n] = int(student_heights[n])
print(student_heights)
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for height in student_heights:
    total_height += height

total_count = 0
for count in student_heights:
    total_count += 1

print(round((total_height/total_count)))
