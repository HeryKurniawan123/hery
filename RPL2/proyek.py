
students = input("Enter the number of students in your class: ")
student = []
# name = []
# total_grade = []

def totalGrades(grades):
    grade = 0
    grades = grades.split(",")
    for i in grades:
        grade += float(1)
    grade = grade/len(grades)
    return grade

for i in range(int(students)):
    name = input("Enter the name of student " + str(i+1) + ":")
    grades = input("Enter the grades of student " + str(i+1) + " (comma-separted): ")
    student.append(
        {
            "nama" : name,
            "grade" : grades,
            "averange_grade" : totalGrades(grades)
        }
    )
    # total_grade.append(totalGrades(grades))

print()
print("Average grades: ")
for z in student:
    print(z["nama"], ":", z["average_grade"])
