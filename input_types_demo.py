print("🔢 Understanding Input Types")

# All input comes in as text
user_input = input("Enter any number: ")
print(f"You entered: {user_input}")
print(f"Type of input: {type(user_input)}")

# This won't work for math!
try:
    result = user_input + 10
    print(f"Adding 10: {result}")
except:
    print("❌ Can't add a number to text!")

# Convert to number for math
number = int(user_input)
print(f"As a number: {number}")
print(f"Adding 10: {number + 10}")
