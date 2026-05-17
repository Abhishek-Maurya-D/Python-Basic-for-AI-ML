students = {
    "Abhishek" : 45,
    "Ankur" : 32,
    "Anuj" : 65,
    "Amit" : 90
}
print("A - Add a student")
print("B - Update marks")
print("C - Search for a Student")
print("D - Display all Students and marks")

op = input("Choose the Operation: ")

if op == 'A':
    name = input("Enter the Name of the Student: ")
    marks = int(input("Enter the Marks of the Student: "))
    new_student = {name:marks}
    students.update(new_student)
elif op == 'B':
    print(students)
    name = input("Enter the Name of the Student to which marks is updated: ")
    if name in students:
        marks = int(input("Enter the new Marks of the Student: "))
        students[name] = marks
elif op == 'C':
    name = input("Enter the Name of the Student to be searched:")
    if name in students:
        print(students.get(name))
elif op == 'D':
    for key, value in students.items():
        print(f"{key} : {value}")
else:
    print("Invalid Option Chosen")