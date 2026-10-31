print("🔢 Number Category Demo")

number = float(input("Enter a number: "))

# CORRECT order (specific to general)
if number > 100:
    print("🚀 That's a big number!")
elif number > 50:
    print("📈 That's a medium-large number!")
elif number > 0:
    print("➕ That's a positive number!")
else:
    print("🔽 That's zero or negative!")

print("\n💡 Try the same number with different ordering...")
