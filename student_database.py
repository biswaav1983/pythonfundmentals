print("🎓 Student Information Database")
print("=" * 40)

students = []

while True:
    print(f"\n📝 Enter information for student #{len(students) + 1}:")

    # Collect student data
    name = input("👤 Full name: ").title()

    # Age with validation
    while True:
        try:
            age = int(input("🎂 Age: "))
            if 16 <= age <= 100:
                break
            else:
                print("❌ Please enter an age between 16 and 100")
        except ValueError:
            print("❌ Please enter a valid number")

    # GPA with validation
    while True:
        try:
            gpa = float(input("📊 GPA (0.0-4.0): "))
            if 0.0 <= gpa <= 4.0:
                break
            else:
                print("❌ GPA must be between 0.0 and 4.0")
        except ValueError:
            print("❌ Please enter a valid number")

    # Major
    major = input("📚 Major: ").title()

    # Graduation year
    while True:
        try:
            grad_year = int(input("🎓 Expected graduation year: "))
            if 2024 <= grad_year <= 2030:
                break
            else:
                print("❌ Please enter a year between 2024 and 2030")
        except ValueError:
            print("❌ Please enter a valid year")

    # Calculate additional info
    years_to_graduation = grad_year - 2024
    gpa_percentage = (gpa / 4.0) * 100

    # Store student data
    student = {
        'name': name,
        'age': age,
        'gpa': gpa,
        'major': major,
        'grad_year': grad_year,
        'years_to_grad': years_to_graduation,
        'gpa_percentage': gpa_percentage
    }
    students.append(student)

    # Add another student?
    add_another = input("\n➕ Add another student? (yes/no): ").lower()
    if add_another not in ['yes', 'y']:
        break

# Display all students
print("\n" + "=" * 70)
print("📋 STUDENT DATABASE SUMMARY")
print("=" * 70)

print(f"{'Name':<20} {'Age':>5} {'GPA':>6} {'Major':<15} {'Grad':>6} {'Status':<12}")
print("-" * 70)

for student in students:
    # Determine academic status
    if student['gpa'] >= 3.5:
        status = "Excellent"
    elif student['gpa'] >= 3.0:
        status = "Good"
    elif student['gpa'] >= 2.0:
        status = "Satisfactory"
    else:
        status = "Needs Help"

    print(f"{student['name']:<20} "
          f"{student['age']:>5} "
          f"{student['gpa']:>6.2f} "
          f"{student['major']:<15} "
          f"{student['grad_year']:>6} "
          f"{status:<12}")

# Statistics
if students:
    avg_age = sum(s['age'] for s in students) / len(students)
    avg_gpa = sum(s['gpa'] for s in students) / len(students)

    print("\n" + "📊 " * 20)
    print("STATISTICS")
    print("📊 " * 20)
    print(f"Total students: {len(students)}")
    print(f"Average age: {avg_age:.1f} years")
    print(f"Average GPA: {avg_gpa:.2f} ({(avg_gpa/4.0)*100:.1f}%)")

    # Find highest and lowest GPA
    highest_gpa_student = max(students, key=lambda s: s['gpa'])
    lowest_gpa_student = min(students, key=lambda s: s['gpa'])

    print(f"Highest GPA: {highest_gpa_student['name']} ({highest_gpa_student['gpa']:.2f})")
    print(f"Lowest GPA: {lowest_gpa_student['name']} ({lowest_gpa_student['gpa']:.2f})")

print("\n🎉 Database complete! Thanks for using the Student Information System!")
