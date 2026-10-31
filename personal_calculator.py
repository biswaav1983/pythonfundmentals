print("🧮 Personal Calculator")

name = input("What's your name? ")
print(f"Hello {name}! I'm your personal calculator.")

while True:
    print(f"\n{name}, what would you like to calculate?")

    num1 = float(input("First number: "))
    operation = input("Operation (+, -, *, /): ")
    num2 = float(input("Second number: "))

    if operation == "+":
        result = num1 + num2
        print(f"{name}, {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{name}, {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{name}, {num1} × {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"{name}, {num1} ÷ {num2} = {result}")
        else:
            print(f"Sorry {name}, I can't divide by zero!")
    else:
        print(f"Sorry {name}, I don't understand that operation.")

    again = input(f"\n{name}, calculate again? (yes/no): ").lower()
    if again != "yes":
        print(f"Goodbye {name}! Thanks for using your personal calculator! 👋")
        break
