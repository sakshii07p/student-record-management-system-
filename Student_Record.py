import json
import os

DATA_FILE = "students.json"


# ─────────────────────────────────────────────
# File Handling
# ─────────────────────────────────────────────

def load_students():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_students(students):
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


# ─────────────────────────────────────────────
# Display Menu
# ─────────────────────────────────────────────

def display_menu():
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("============================================")


# ─────────────────────────────────────────────
# Add Student
# ─────────────────────────────────────────────

def add_student(students):
    print("\n--- Add Student ---")

    while True:
        student_id = input("Enter Student ID: ").strip()
        if not student_id.isdigit():
            print("Invalid Input. Student ID must be a number.")
            continue
        student_id = int(student_id)
        if any(s["id"] == student_id for s in students):
            print("Student ID already exists. Please enter a unique ID.")
            continue
        break

    while True:
        name = input("Enter Name: ").strip()
        if not name:
            print("Invalid Input. Name cannot be empty.")
        else:
            break

    while True:
        age = input("Enter Age: ").strip()
        if not age.isdigit() or int(age) <= 0 or int(age) > 100:
            print("Invalid Input. Please enter a valid age (1-100).")
        else:
            age = int(age)
            break

    while True:
        course = input("Enter Course: ").strip()
        if not course:
            print("Invalid Input. Course cannot be empty.")
        else:
            break

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    save_students(students)
    print("Student Added Successfully.")


# ─────────────────────────────────────────────
# View Students
# ─────────────────────────────────────────────

def view_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No Student Records Found.")
        return

    for s in students:
        print("-" * 30)
        print(f"Student ID : {s['id']}")
        print(f"Name       : {s['name']}")
        print(f"Age        : {s['age']}")
        print(f"Course     : {s['course']}")
    print("-" * 30)


# ─────────────────────────────────────────────
# Search Student
# ─────────────────────────────────────────────

def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID: ").strip()

    if not student_id.isdigit():
        print("Invalid Input. Student ID must be a number.")
        return

    student_id = int(student_id)
    for s in students:
        if s["id"] == student_id:
            print("\nStudent Found")
            print("-" * 30)
            print(f"Student ID : {s['id']}")
            print(f"Name       : {s['name']}")
            print(f"Age        : {s['age']}")
            print(f"Course     : {s['course']}")
            print("-" * 30)
            return

    print("Student Not Found.")


# ─────────────────────────────────────────────
# Update Student
# ─────────────────────────────────────────────

def update_student(students):
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID to Update: ").strip()

    if not student_id.isdigit():
        print("Invalid Input. Student ID must be a number.")
        return

    student_id = int(student_id)
    for s in students:
        if s["id"] == student_id:
            print(f"Updating record for: {s['name']}")

            while True:
                new_name = input(f"Enter New Name (current: {s['name']}): ").strip()
                if not new_name:
                    print("Invalid Input. Name cannot be empty.")
                else:
                    break

            while True:
                new_age = input(f"Enter New Age (current: {s['age']}): ").strip()
                if not new_age.isdigit() or int(new_age) <= 0 or int(new_age) > 100:
                    print("Invalid Input. Please enter a valid age (1-100).")
                else:
                    new_age = int(new_age)
                    break

            while True:
                new_course = input(f"Enter New Course (current: {s['course']}): ").strip()
                if not new_course:
                    print("Invalid Input. Course cannot be empty.")
                else:
                    break

            s["name"] = new_name
            s["age"] = new_age
            s["course"] = new_course
            save_students(students)
            print("Student Updated Successfully.")
            return

    print("Student Not Found.")


# ─────────────────────────────────────────────
# Delete Student
# ─────────────────────────────────────────────

def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID to Delete: ").strip()

    if not student_id.isdigit():
        print("Invalid Input. Student ID must be a number.")
        return

    student_id = int(student_id)
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            print("Student Deleted Successfully.")
            return

    print("Student Not Found.")


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main():
    students = load_students()

    while True:
        display_menu()
        choice = input("Enter Choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid Input. Please Try Again.")


if __name__ == "__main__":
    main()