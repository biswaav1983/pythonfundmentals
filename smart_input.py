print("🧠 Smart Data Input System")

def get_string(prompt):
    """Get a string input with validation"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("❌ Please enter some text.")

def get_integer(prompt):
    """Get an integer input with validation"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Please enter a whole number.")

def get_float(prompt, min_val=None, max_val=None):
    """Get a float input with validation"""
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"❌ Please enter a number at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"❌ Please enter a number at most {max_val}.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number.")

def get_yes_no(prompt):
    """Get a yes/no input and return True/False"""
    while True:
        answer = input(prompt + " (yes/no): ").lower().strip()
        if answer in ['yes', 'y', 'true', '1']:
            return True
        elif answer in ['no', 'n', 'false', '0']:
            return False
        else:
            print("❌ Please answer yes or no.")

# Use our smart input functions
print("Let's collect some information about you:")

name = get_string("👤 Your name: ")
age = get_integer("🎂 Your age: ")
gpa = get_float("📚 Your GPA (0.0-4.0): ", min_val=0.0, max_val=4.0)
is_working = get_yes_no("💼 Are you currently working?")

print(f"\n✅ Information collected successfully!")
print(f"   Name: {name} ({type(name).__name__})")
print(f"   Age: {age} ({type(age).__name__})")
print(f"   GPA: {gpa} ({type(gpa).__name__})")
print(f"   Working: {is_working} ({type(is_working).__name__})")
