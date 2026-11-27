
student_name = "Kowshalya"

marks = [85, 90, 78, 92, 88]

total = sum(marks)
average = total / len(marks)

print("===== STUDENT RESULT =====")
print("Student Name:", student_name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
else:
    print("Grade: D")

print("Result Generated Successfully!")
