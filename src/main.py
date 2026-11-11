from calculator import add_student, update_student, delete_student, search_student, check_pass_fail

def main():
    print("Welcome to the Student Grading System")

    while True:
        print("\n1. Add Student")
        print("2. Update Grades")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            math = input("Enter Math grade: ")
            english = input("Enter English grade: ")
            if student_id and name and math and english:
                grades = "Math:" + math + ",English:" + english
                add_student(student_id, name, grades)
                print("Student added.")
            else:
                print("All fields are required.")

        elif choice == "2":
            student_id = input("Enter student ID to update: ")
            math = input("Enter new Math grade: ")
            english = input("Enter new English grade: ")
            if student_id and math and english:
                new_grades = "Math:" + math + ",English:" + english
                update_student(student_id, new_grades)
                print("Grades updated.")
            else:
                print("All fields are required.")

        elif choice == "3":
            student_id = input("Enter ID to delete: ")
            delete_student(student_id)
            print("Student deleted.")

        elif choice == "4":
            search_input = input("Enter name or ID to search: ")
            results = search_student(search_input)
            if results:
                for student in results:
                    print("\nID:", student[0])
                    print("Name:", student[1])
                    print("Grades:")
                    check_pass_fail(student[2])
            else:
                print("Student not found.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
