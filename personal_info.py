print("📋 Personal Information Collector")
print("=" * 40)

# Collect basic information
print("Let's get to know you better!")
name = input("👤 Full name: ")
age = int(input("🎂 Age: "))
email = input("📧 Email: ")
phone = input("📱 Phone number: ")

# Collect preferences
print(f"\nThanks {name}! Now some preferences:")
favorite_color = input("🎨 Favorite color: ")
hobby = input("🎯 Main hobby: ")
dream_job = input("💼 Dream job: ")

# Calculate some fun facts
birth_year = 2024 - age
next_birthday_age = age + 1

# Display summary
print("\n" + "=" * 50)
print("📊 YOUR PERSONAL PROFILE")
print("=" * 50)

print(f"Name: {name}")
print(f"Age: {age} years old (born around {birth_year})")
print(f"Next birthday: You'll turn {next_birthday_age}!")
print(f"Contact: {email} | {phone}")

print(f"\n🎨 Personality:")
print(f"   • Loves the color {favorite_color}")
print(f"   • Enjoys {hobby}")
print(f"   • Dreams of being a {dream_job}")

print(f"\n🌟 Fun Facts:")
print(f"   • {name} has been alive for approximately {age * 365} days!")
print(f"   • In 10 years, {name} will be {age + 10} years old")
print(f"   • {name}'s favorite color is {favorite_color} - great choice!")

print("\n" + "🎉 " * 20)
print(f"Nice to meet you, {name}! Keep pursuing that {dream_job} dream!")
