class StudentManagement:
    def __init__(self):
        self.username = "admin"
        self.password = "admin123"

    def login(self):
        uname = input("Enter admin username: ")
        pwd = input("Enter admin password: ")

        if uname == self.username and pwd == self.password:
            print("Login successful!\n")
            self.menu()
        else:
            print("Invalid credentials!")

    def menu(self):
        while True:
            print("\n--- Student Management Menu ---")
            print("1. Add Student")
            print("2. View Students")
            print("3. Delete Student")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again!")

    def add_student(self):
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        grade = input("Enter grade: ")
        course = input("Enter course: ")
        email_id = input("Enter email ID: ")
        semester = input("Enter semester: ")

        with open("students.txt", "a") as file:
            file.write(f"{name},{roll},{grade},{course},{email_id},{semester}\n")
        print("Student added successfully.")

    def view_students(self):
        print("\n--- Student List ---")
        try:
            with open("students.txt", "r") as file:
                lines = file.readlines()
                if not lines:
                    print("No student records found.")
                    return
                for line in lines:
                    try:
                        name, roll, grade, course, email_id, semester = line.strip().split(",")
                        print(f"Name: {name}, Roll: {roll}, Grade: {grade}, Course: {course}, Email ID: {email_id}, Semester: {semester}")
                    except ValueError:
                        continue
        except FileNotFoundError:
            print("No student records found.")

    def delete_student(self):
        roll = input("Enter roll number to delete: ")
        try:
            with open("students.txt", "r") as file:
                lines = file.readlines()

            found = False
            with open("students.txt", "w") as file:
                for line in lines:
                    if roll != line.strip().split(",")[1]:
                        file.write(line)
                    else:
                        found = True

            if found:
                print("Student deleted.")
            else:
                print("Roll number not found.")
        except FileNotFoundError:
            print("No student records found.")



system = StudentManagement()
system.login()
