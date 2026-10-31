print("🎢 Amusement Park Ride Checker")

age = int(input("How old are you? "))
height = float(input("How tall are you in cm? "))

if age >= 12 and height >= 140:
    print("🎉 You can ride the roller coaster!")
    print("   Have fun and stay safe!")
else:
    print("😔 Sorry, you don't meet the requirements.")
    if age < 12:
        print("   You need to be at least 12 years old.")
    if height < 140:
        print("   You need to be at least 140cm tall.")

print("\n🎠 Enjoy the amusement park!")
