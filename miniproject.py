students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    python = int(input("Enter Python marks: "))
    math = int(input("Enter Math marks: "))
    english = int(input("Enter English marks: "))
    
    total = python + math + english
    average = total / 3

    if average >= 90:
        grade = 'A+'
    elif average >= 75:
        grade = 'A'
    elif average >= 60:
        grade = 'B'
    elif average >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    students[roll] = {
        "Name": name,
        "Python": python,
        "Math": math,
        "English": english,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    print(" Student added successfully!\n")

def view_all_students():
    if not students:
        print("No students found.")
        return
    for roll, info in students.items():
        print(f"\nRoll: {roll}")
        for key, value in info.items():
            print(f"{key}: {value}")
        print("--------------------------")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        info = students[roll]
        print(f"\nStudent Details for Roll: {roll}")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print(" Student not found.")

def main():
    while True:
        print("\n--- Student Result Management ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by Roll No")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            print("Goodbye, tiger! ")
            break
        else:
            print("Invalid choice! Try again.")

main()
