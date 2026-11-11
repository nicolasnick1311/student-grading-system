import csv

def load_students():
    students = []
    try:
        file = open("students.csv", "r")
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            students.append(row)
        file.close()
    except FileNotFoundError:
        pass
    return students

def save_students(students):
    file = open("students.csv", "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Grades"])
    for student in students:
        writer.writerow(student)
    file.close()

def add_student(student_id, name, grades):
    students = load_students()
    students.append([student_id, name, grades])
    save_students(students)

def update_student(student_id, new_grades):
    students = load_students()
    for student in students:
        if student[0] == student_id:
            student[2] = new_grades
    save_students(students)

def delete_student(student_id):
    students = load_students()
    updated = []
    for student in students:
        if student[0] != student_id:
            updated.append(student)
    save_students(updated)

def search_student(search_input):
    students = load_students()
    found = []
    for student in students:
        if search_input.lower() in student[1].lower() or student[0] == search_input:
            found.append(student)
    return found

def check_pass_fail(grades):
    if "Math:" in grades and "English:" in grades:
        parts = grades.split(",")
        for subject in parts:
            if "Math" in subject:
                math_mark = int(subject.replace("Math:", ""))
                if math_mark >= 40:
                    print("Math: Passed")
                else:
                    print("Math: Failed")
            if "English" in subject:
                eng_mark = int(subject.replace("English:", ""))
                if eng_mark >= 40:
                    print("English: Passed")
                else:
                    print("English: Failed")
