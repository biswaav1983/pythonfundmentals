print("🎫 Event Discount Checker")

is_student = input("Are you a student? (yes/no): ").lower() == "yes"
is_senior = int(input("What's your age? ")) >= 65

if is_student or is_senior:
    print("🎉 You qualify for a discount!")
    if is_student:
        print("   Student discount: 20% off")
    if is_senior:
        print("   Senior discount: 15% off")
    if is_student and is_senior:
        print("   Amazing! You get both discounts!")
else:
    print("💰 Regular price applies.")
    print("   But the event will still be great!")

print("\n🎊 Enjoy the event!")
