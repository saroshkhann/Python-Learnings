class Student:
    def __init__(self):
        self.students  = []

    def menu(self):
        print("1. Add Student")
        print("2. Add Course")
        print("3. View Students")
        print("4. View Student Details")
        print("5. Show Topper")
        print("6. Exit")

    def add_student(self):
        student_name = input("Enter student name: ")
        student_id = int(input("Enter student ID: "))

        for student in self.students:
            if student["id"] == student_id:
                print("Student ID already exists!")
                return

        self.students.append({"name": student_name, "id": student_id, "courses": []})
        print(self.students)
        print("Student added successfully!")

    def add_course(self):
        id_of_student = int(input("Enter student ID: "))
        course_name = input("Enter course name: ")
        marks = int(input("Enter marks: "))

        if marks > 0 and marks < 100:
            found = False

            for student in self.students:
                if student["id"] == id_of_student:
                    found = True
                    student["courses"].append({"course": course_name, "marks": marks})
                    print(self.students)

            if not found:
                print("Student not found!")
        else:
            print("Enter valid marks (0-100!)")


    def view_students(self):
        print("Students List: ")
        found = False
        counter = 1
        for student in self.students:
            found = True
            print(f"{counter}. {student['name']} (ID: {student['id']})")
            counter+=1

        if not found:
            print("No students found!")

    def view_student_details(self):
        for_id = int(input("Enter student ID: "))
        found =False

        for student in self.students:
            if student["id"] == for_id:
                found = True
                print(f"Name: {student['name']}")
                print(f"Courses: ")
                index = 0

                if len(student["courses"]) == 0 :
                    print("No courses added yet! ")
                else:
                    while index != len(student["courses"]):
                        print(f"{student["courses"][index]["course"]} - {student["courses"][index]["marks"]}")
                        index+=1
                total = 0
                count = 0
                for course in student["courses"]:
                    total += course["marks"]
                    count += 1

                if count > 0:
                    average = total / count
                    print(f"Average Marks: {average}")
        if not found:
            print("Student not found!")

    def show_topper(self):
        print("Topper Student: ")
        highest_avg = 0
        topper_name = ""
        for student in self.students:
            total = 0
            count = 0
            for course in student["courses"]:
                total += course["marks"]
                count += 1

            if count > 0:
                avg = total / count

                if avg > highest_avg:
                    highest_avg = avg
                    topper_name = student["name"]
        if topper_name == "":
            print("No students available!")
        else:
            print(f"Topper: {topper_name}")
            print(f"Average Marks: {highest_avg}")

