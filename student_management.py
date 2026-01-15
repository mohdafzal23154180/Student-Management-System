
  # Student Management System using Python

FILE_NAME = "students.txt"

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{course},{marks}\n")

    print("✅ Student added successfully\n")


def view_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()
            if not students:
                print("No student records found\n")
                return

            print("\n--- Student Records ---")
            for student in students:
                roll, name, course, marks = student.strip().split(",")
                print(f"Roll: {roll}, Name: {name}, Course: {course}, Marks: {marks}")
            print()
    except FileNotFoundError:
        print("No data file found\n")


def update_student():
    roll_to_update = input("Enter Roll Number to Update: ")
    updated_students = []
    found = False

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    for student in students:
        roll, name, course, marks = student.strip().split(",")
        if roll == roll_to_update:
            print("Enter new details:")
            name = input("New Name: ")
            course = input("New Course: ")
            marks = input("New Marks: ")
            updated_students.append(f"{roll},{name},{course},{marks}\n")
            found = True
        else:
            updated_students.append(student)

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_students)

    if found:
        print("✅ Student updated successfully\n")
    else:
        print("❌ Student not found\n")


def delete_student():
    roll_to_delete = input("Enter Roll Number to Delete: ")
    new_students = []
    found = False

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    for student in students:
        roll, name, course, marks = student.strip().split(",")
        if roll != roll_to_delete:
            new_students.append(student)
        else:
            found = True

    with open(FILE_NAME, "w") as file:
        file.writelines(new_students)

    if found:
        print("✅ Student deleted successfully\n")
    else:
        print("❌ Student not found\n")


def main_menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Thank you! Exiting program...")
            break
        else:
            print("❌ Invalid choice. Try again.\n")


# Program starts here
main_menu()
        

          