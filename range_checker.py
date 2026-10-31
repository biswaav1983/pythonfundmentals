print("🎯 Number Range Checker")

number = float(input("Enter a number: "))

if number >= 1 and number <= 10:
    print(f"✅ {number} is between 1 and 10!")
    print("   This number is in the valid range.")
elif number >= 11 and number <= 20:
    print(f"📈 {number} is between 11 and 20!")
    print("   This is in the higher range.")
elif number >= 0 and number < 1:
    print(f"🔸 {number} is between 0 and 1!")
    print("   This is a small positive number.")
else:
    print(f"🔍 {number} is outside our ranges!")
    print("   This number is either negative or greater than 20.")

print(f"\n💫 You entered: {number}")
