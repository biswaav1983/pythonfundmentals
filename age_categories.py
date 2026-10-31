print("👥 Age Category System")

age = int(input("Enter age: "))

if age < 0:
    print("⚠️ Invalid age! Age cannot be negative.")
elif age <= 2:
    print("👶 Baby - Sleep, eat, and grow!")
elif age <= 12:
    print("🧒 Child - Play, learn, and explore!")
elif age <= 17:
    print("🧑 Teenager - Study, discover yourself!")
elif age <= 64:
    print("👨 Adult - Work, build, and achieve!")
elif age <= 100:
    print("👴 Senior - Enjoy wisdom and experience!")
else:
    print("🎂 Wow! You're a centenarian! Amazing!")

print(f"\n🎉 Age: {age} years young!")
