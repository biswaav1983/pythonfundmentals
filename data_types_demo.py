print("🔍 Data Types Explorer")

# Different types of data
name = "Alice"                    # String
age = 25                         # Integer
height = 5.6                     # Float
is_student = True                # Boolean

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Is student: {is_student} (type: {type(is_student).__name__})")

print("\n💡 What each type can do:")

# String operations
print(f"String length: {len(name)} characters")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")

# Number operations
print(f"Age in dog years: {age * 7}")
print(f"Height in cm: {height * 30.48}")

# Boolean operations
print(f"Opposite of is_student: {not is_student}")
print(f"Is adult: {age >= 18}")
