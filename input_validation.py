print("🎯 Age Category Classifier")
print("(With input validation)")

while True:
    age_input = input("Enter your age: ")

    # Check if input is valid
    if age_input.isdigit():
        age = int(age_input)
        if age >= 0 and age <= 150:
            break
        else:
            print("❌ Please enter a realistic age (0-150)")
    else:
        print("❌ Please enter a valid number")

# Now we have valid input
print(f"\n✅ Valid age received: {age}")

# Classify the age
if age < 13:
    category = "Child"
    emoji = "🧒"
    message = "Enjoy being young and learning!"
elif age < 20:
    category = "Teenager"
    emoji = "🧑"
    message = "These are exciting years of growth!"
elif age < 60:
    category = "Adult"
    emoji = "👨"
    message = "You're in your prime years!"
else:
    category = "Senior"
    emoji = "👴"
    message = "Wisdom comes with experience!"

print(f"\n{emoji} Category: {category}")
print(f"💭 {message}")
print(f"🎂 You've been on Earth for {age} years!")
