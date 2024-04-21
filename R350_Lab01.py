# Function to create a new student record
def create_student_record():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    class_name = input("Enter class: ")
    gpa = float(input("Enter GPA: "))
    return {'ID': student_id, 'Name': name, 'Class': class_name, 'GPA': gpa}

# Function to insert a new student record
def insert_student_record(records, record):
    records.append(record)
    print("Student record inserted successfully!")

# Function to delete a student record
def delete_student_record(records, student_id):
    for record in records:
        if record['ID'] == student_id:
            records.remove(record)
            print("Student record deleted successfully!")
            return
    print("Student not found!")

# Function to update a student record
def update_student_record(records, student_id):
    for record in records:
        if record['ID'] == student_id:
            name = input("Enter updated name: ")
            class_name = input("Enter updated class: ")
            gpa = float(input("Enter updated GPA: "))
            record['Name'] = name
            record['Class'] = class_name
            record['GPA'] = gpa
            print("Student record updated successfully!")
            return
    print("Student not found!")

# Function to display all student records
def display_student_records(records):
    if len(records) == 0:
        print("No student records found!")
    else:
        print("Student Records:")
        for record in records:
            print("ID:", record['ID'])
            print("Name:", record['Name'])
            print("Class:", record['Class'])
            print("GPA:", record['GPA'])
            print()

# Function to search for a student record by ID
def search_student_record(records, student_id):
    for record in records:
        if record['ID'] == student_id:
            print("Student Record Found:")
            print("ID:", record['ID'])
            print("Name:", record['Name'])
            print("Class:", record['Class'])
            print("GPA:", record['GPA'])
            return
    print("Student not found!")

# Main function to run the program
def main():
    student_records = []
    while True:
        print("\n--- Student Record Management ---")
        print("1. Create a new student record")
        print("2. Insert a student record")
        print("3. Delete a student record")
        print("4. Update a student record")
        print("5. Display all student records")
        print("6. Search for a student record")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            record = create_student_record()
            insert_student_record(student_records, record)
        elif choice == '2':
            record = create_student_record()
            insert_student_record(student_records, record)
        elif choice == '3':
            student_id = input("Enter student ID to delete: ")
            delete_student_record(student_records, student_id)
        elif choice == '4':
            student_id = input("Enter student ID to update: ")
            update_student_record(student_records, student_id)
        elif choice == '5':
            display_student_records(student_records)
        elif choice == '6':
            student_id = input("Enter student ID to search: ")
            search_student_record(student_records, student_id)
        elif choice == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == '__main__':
    main()