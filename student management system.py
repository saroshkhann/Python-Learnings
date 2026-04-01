from studentdetails import Student

student = Student()

is_on = True

while is_on:
    student.menu()
    choice = int(input("Enter the operation you want to perform"))
    if choice == 1:
        student.add_student()
    elif choice == 2:
        student.add_course()
    elif choice == 3:
        student.view_students()
    elif choice == 4:
        student.view_student_details()
    elif choice == 5:
        student.show_topper()
    else:
        print("Exiting program... Goodbye!")
        is_on = False