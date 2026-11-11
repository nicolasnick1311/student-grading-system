from calculator import add_student, search_student
from unittest.mock import patch, mock_open

def test_add_student_input():
    with patch('builtins.input', side_effect=["201", "Alice", "Math:85,English:35"]):
        student_id = input("Enter ID: ")
        name = input("Enter name: ")
        grades = input("Enter grades: ")
        add_student(student_id, name, grades)
        print("Input test passed.")

def test_add_student_file_write():
    m = mock_open()
    with patch('builtins.open', m):
        add_student("202", "Bob", "Math:60,English:70")
        m.assert_called_with('students.csv', 'w', newline="")
        print("File write test passed.")

@patch('builtins.open', new_callable=mock_open, read_data="ID,Name,Grades\n203,Charlie,Math:80,English:90\n")
def test_search_student(mock_file):
    result = search_student("Charlie")
    if result and result[0][1] == "Charlie":
        print("Search test passed.")
    else:
        print("Search test failed.")

test_add_student_input()
test_add_student_file_write()
test_search_student()
