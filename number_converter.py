print("🧮 Simple Calculator")

# Get numbers from user
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")

print(f"\nAs text: {first_number} + {second_number} = {first_number + second_number}")

# Convert to numbers for real math
num1 = float(first_number)
num2 = float(second_number)
result = num1 + num2

print(f"As numbers: {num1} + {num2} = {result}")

# You can also convert directly
print("\n🎯 Let's try multiplication:")
num3 = float(input("Enter a number: "))
num4 = float(input("Enter another number: "))
print(f"{num3} × {num4} = {num3 * num4}")
