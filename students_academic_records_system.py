
# Define an empty dictionary to store student records
students = {}

def add_student():
    """Add a new student to the system"""
    # Get student ID from user
    student_id = input("Enter Student ID: ")
    
    # Check if student ID already exists
    if student_id in students:
        print("Student ID already exists!")
        return
    
    # Get student details from user
    name = input("Enter Full Name: ")
    student_class = input("Enter Class: ")
    subjects = {}
    
    # Get number of subjects and their marks
    num_subjects = int(input("Enter number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Enter Subject Name: ")
        mark = float(input(f"Enter {subject} marks: "))
        subjects[subject] = mark
    
    # Store student record in dictionary
    students[student_id] = {
        "name": name,
        "class": student_class,
        "subjects": subjects
    }
    print("Student added successfully!")

def view_all_students():
    """Display all students with their IDs and names"""
    # Check if there are any students
    if not students:
        print("No students found!")
        return
    
    # Print student list
    print("Student List:")
    for student_id, student in students.items():
        print(f"ID: {student_id}, Name: {student['name']}")

def view_student_report():
    """Display a student's report"""
    # Get student ID from user
    student_id = input("Enter Student ID: ")
    
    # Check if student exists
    if student_id not in students:
        print("Student not found!")
        return
    
    # Get student record
    student = students[student_id]
    print(f"Name: {student['name']}, Class: {student['class']}")
    print("Subjects and Marks:")
    
    # Calculate total marks and average
    total = 0
    for subject, mark in student['subjects'].items():
        print(f"{subject}: {mark}")
        total += mark
    
    average = total / len(student['subjects'])
    grade = calculate_grade(average)
    print(f"Total: {total}, Average: {average:.2f}, Grade: {grade}")

def calculate_grade(average):
    """Calculate grade based on average marks"""
    # Determine grade based on average marks
    if 75 <= average <= 100:
        return 'A'
    elif 65 <= average < 75:
        return 'B'
    elif 50 <= average < 65:
        return 'C'
    elif 40 <= average < 50:
        return 'D'
    else:
        return 'F'

def update_marks():
    """Update marks for an existing subject"""
    # Get student ID from user
    student_id = input("Enter Student ID: ")
    
    # Check if student exists
    if student_id not in students:
        print("Student not found!")
        return
    
    # Get subject and new marks from user
    subject = input("Enter Subject Name: ")
    if subject not in students[student_id]['subjects']:
        print("Subject not found!")
        return
    
    new_mark = float(input(f"Enter new marks for {subject}: "))
    students[student_id]['subjects'][subject] = new_mark
    print("Marks updated successfully!")

def delete_student():
    """Delete a student record"""
    # Get student ID from user
    student_id = input("Enter Student ID: ")
    
    # Check if student exists
    if student_id not in students:
        print("Student not found!")
        return
    
    # Delete student record
    del students[student_id]
    print("Student record deleted successfully!")

def main():
    # Main loop to display menu and handle user input
    while True:
        print("\nStudent Academic Record Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. View Student Report")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            view_student_report()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
