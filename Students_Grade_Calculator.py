num_students = int(input("Number of Students: "))
students = []
for i in range(num_students):
    name = str(input("Name: "))
    scores = list(map(int, input("Enter scores (Math, English, Science): ").split()))
    average = sum(scores)/len(scores)
    students.append({"name": name, "scores": scores, "average": average})
for student in students:
    print(f"{student["name"]} {student["scores"]} | Average: {student["average"]}")
class_average = sum(s["average"] for s in students) / num_students
print(f"Class average: {class_average}")
top_student = max(students, key=lambda s: ["average"])
lowest_student = min(students, key=lambda s: s["average"])
print(f"Top Student: {top_student['name']} ({top_student['average']})")
print(f"Lowest Student: {lowest_student["name"]} ({lowest_student["average"]})")