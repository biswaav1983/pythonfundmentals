print("🧮 Simple Calculator")

num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
    print(f"➕ {num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"➖ {num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"✖️ {num1} × {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"➗ {num1} ÷ {num2} = {result}")
    else:
        print("⚠️ Cannot divide by zero!")
else:
    print("❌ Invalid operation! Use +, -, *, or /")

print("\n🎯 Calculation complete!")
