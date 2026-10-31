print("🏪 Store Access System")

age = int(input("Enter your age: "))
has_id = input("Do you have ID? (yes/no): ").lower() == "yes"
is_member = input("Are you a store member? (yes/no): ").lower() == "yes"

# Complex condition: (18+ with ID) OR (any age if member)
if (age >= 18 and has_id) or is_member:
    print("✅ Welcome to the store!")

    if is_member:
        print("   Member benefits: 10% discount on all items!")

    if age >= 18 and has_id:
        print("   You can purchase age-restricted items.")

    if not has_id and is_member:
        print("   Reminder: Bring ID next time for full access.")

else:
    print("❌ Sorry, you cannot enter the store.")
    print("   You need to be 18+ with ID, OR be a member.")

print("\n🛍️ Thank you for visiting!")
