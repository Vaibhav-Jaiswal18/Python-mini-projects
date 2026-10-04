students = []

college_info = (
    "ABC Institute of Technology",
    "Lucknow",
    "Computer Science Department"
)

courses = set()


# ---------------- ADD STUDENT ----------------
def add_student():

    print("\nEnter Student Details")

    roll = int(input("Roll Number : "))
    name = input("Name : ").title()
    age = int(input("Age : "))
    course = input("Course : ").title()
    marks = float(input("Marks : "))

    grade = ""

    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else:
        grade = "D"

    student = {
        "Roll": roll,
        "Name": name,
        "Age": age,
        "Course": course,
        "Marks": marks,
        "Grade": grade
    }

    students.append(student)
    courses.add(course)

    print("Student Record Added Successfully.")


# ---------------- DISPLAY STUDENTS ----------------
def display_students():

    if len(students) == 0:
        print("\nNo Records Found.")
        return

    print("\n---------------- Student Records ----------------")

    for student in students:

        print("------------------------------------------")
        print("Roll   :", student["Roll"])
        print("Name   :", student["Name"])
        print("Age    :", student["Age"])
        print("Course :", student["Course"])
        print("Marks  :", student["Marks"])
        print("Grade  :", student["Grade"])


# ---------------- SEARCH STUDENT ----------------
def search_student():

    roll = int(input("Enter Roll Number to Search : "))

    found = False

    for student in students:

        if student["Roll"] == roll:

            print("\nStudent Found")
            print(student)

            found = True
            break

    if not found:
        print("Student Record Not Found.")


# ---------------- UPDATE STUDENT ----------------
def update_student():

    roll = int(input("Enter Roll Number to Update : "))

    for student in students:

        if student["Roll"] == roll:

            print("\nEnter New Details")

            student["Name"] = input("New Name : ").title()
            student["Age"] = int(input("New Age : "))
            student["Course"] = input("New Course : ").title()
            student["Marks"] = float(input("New Marks : "))

            courses.add(student["Course"])

            marks = student["Marks"]

            if marks >= 90:
                student["Grade"] = "A+"
            elif marks >= 80:
                student["Grade"] = "A"
            elif marks >= 70:
                student["Grade"] = "B"
            elif marks >= 60:
                student["Grade"] = "C"
            else:
                student["Grade"] = "D"

            print("Record Updated Successfully.")

            return

    print("Student Not Found.")


# ---------------- DELETE STUDENT ----------------
def delete_student():

    roll = int(input("Enter Roll Number to Delete : "))

    for student in students:

        if student["Roll"] == roll:

            students.remove(student)

            print("Record Deleted Successfully.")

            return

    print("Student Not Found.")


# ---------------- SORT BY NAME ----------------
def sort_name():

    if len(students) == 0:
        print("No Records Available.")
        return

    sorted_students = sorted(
        students,
        key=lambda x: x["Name"]
    )

    print("\nStudents Sorted by Name\n")

    for student in sorted_students:
        print(student)


# ---------------- SORT BY MARKS ----------------
def sort_marks():

    if len(students) == 0:
        print("No Records Available.")
        return

    sorted_students = sorted(
        students,
        key=lambda x: x["Marks"],
        reverse=True
    )

    print("\nStudents Sorted by Marks\n")

    for student in sorted_students:
        print(student)


# ---------------- DISPLAY COURSES ----------------
def display_courses():

    if len(courses) == 0:
        print("No Courses Available.")
        return

    print("\nUnique Courses Offered")

    for course in sorted(courses):
        print(course)


# ---------------- COLLEGE DETAILS ----------------
def college_details():

    print("\nCollege Information")

    print("College Name :", college_info[0])
    print("City         :", college_info[1])
    print("Department   :", college_info[2])


# ---------------- TOPPER ----------------
def topper():

    if len(students) == 0:
        print("No Records Found.")
        return

    highest = max(
        student["Marks"]
        for student in students
    )

    print("\nTopper(s)\n")

    for student in students:

        if student["Marks"] == highest:
            print(student)


# ================= MAIN MENU =================

while True:

    print("\n")

    print("=" * 45)
    print(" STUDENT RECORD MANAGEMENT SYSTEM ")
    print("=" * 45)

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort by Name")
    print("7. Sort by Marks")
    print("8. Display Unique Courses")
    print("9. Display College Information")
    print("10. Display Topper")
    print("11. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        sort_name()

    elif choice == "7":
        sort_marks()

    elif choice == "8":
        display_courses()

    elif choice == "9":
        college_details()

    elif choice == "10":
        topper()

    elif choice == "11":

        print("\nThank You for Using the System.")

        break

    else:

        print("Invalid Choice. Please Try Again.")