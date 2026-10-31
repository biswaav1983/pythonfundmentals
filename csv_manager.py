print("📊 CSV Data Manager")

import csv
import os

def create_student_csv():
    """Create a CSV file with student data"""
    filename = "students.csv"

    print("📝 Creating student database...")
    students = []

    while True:
        print(f"\n👤 Enter data for student #{len(students) + 1}:")
        name = input("Name: ")
        age = int(input("Age: "))
        grade = float(input("Grade (0-100): "))
        subject = input("Subject: ")

        students.append([name, age, grade, subject])

        if input("Add another student? (y/n): ").lower() != 'y':
            break

    # Write to CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(['Name', 'Age', 'Grade', 'Subject'])

        # Write student data
        writer.writerows(students)

    print(f"✅ Student data saved to {filename}!")
    return filename

def read_student_csv(filename):
    """Read and display CSV data"""
    if os.path.exists(filename):
        print(f"\n📖 Reading data from {filename}:")

        with open(filename, 'r') as file:
            reader = csv.reader(file)

            # Read header
            header = next(reader)
            print(f"\n{'Name':<15} {'Age':<5} {'Grade':<7} {'Subject':<12}")
            print("-" * 40)

            # Read and display each row
            total_grade = 0
            count = 0

            for row in reader:
                name, age, grade, subject = row
                print(f"{name:<15} {age:<5} {grade:<7} {subject:<12}")
                total_grade += float(grade)
                count += 1

            if count > 0:
                avg_grade = total_grade / count
                print("-" * 40)
                print(f"Average Grade: {avg_grade:.2f}")
                print(f"Total Students: {count}")
    else:
        print(f"❌ File {filename} not found!")

def analyze_csv(filename):
    """Analyze the CSV data"""
    if os.path.exists(filename):
        print(f"\n📊 Analyzing {filename}:")

        subjects = {}
        ages = []
        grades = []

        with open(filename, 'r') as file:
            reader = csv.DictReader(file)  # Use DictReader for easier access

            for row in reader:
                # Count subjects
                subject = row['Subject']
                subjects[subject] = subjects.get(subject, 0) + 1

                # Collect ages and grades
                ages.append(int(row['Age']))
                grades.append(float(row['Grade']))

        print(f"📚 Subjects breakdown:")
        for subject, count in subjects.items():
            print(f"   {subject}: {count} students")

        if ages and grades:
            print(f"\n📈 Statistics:")
            print(f"   Average age: {sum(ages) / len(ages):.1f}")
            print(f"   Average grade: {sum(grades) / len(grades):.2f}")
            print(f"   Highest grade: {max(grades)}")
            print(f"   Lowest grade: {min(grades)}")

# Main program
print("Welcome to the CSV Data Manager!")

while True:
    print("\n" + "📊" * 15)
    print("CSV DATA MANAGER")
    print("📊" * 15)
    print("1. 📝 Create new student CSV")
    print("2. 📖 Read existing CSV")
    print("3. 📊 Analyze CSV data")
    print("4. 🚪 Exit")

    choice = input("\nChoose option (1-4): ")

    if choice == '1':
        csv_file = create_student_csv()
    elif choice == '2':
        filename = input("Enter CSV filename (or press Enter for 'students.csv'): ")
        if not filename:
            filename = "students.csv"
        read_student_csv(filename)
    elif choice == '3':
        filename = input("Enter CSV filename (or press Enter for 'students.csv'): ")
        if not filename:
            filename = "students.csv"
        analyze_csv(filename)
    elif choice == '4':
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice!")
