info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

# list all unique courses
unique_courses = set()
for name, course in info:
    unique_courses.add(course)

print("Unique courses:", unique_courses)

# list students enrolled in english
english_students = set()
for name, course in info:
    if course == "English":
        english_students.add(name)

print("Students Enrolled in English: ", english_students)

# create dictionary (student, set of courses)
student_courses = {}
for name, course in info:
    if student_courses.get(name) == None:
        student_courses[name] = set()
        student_courses[name].add(course)
    else:
        student_courses[name].add(course)

print("Student Courses Dictionary: ", student_courses)