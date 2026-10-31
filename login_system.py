print("🔐 Simple Login System")

# Predefined valid credentials
valid_username = "admin"
valid_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == valid_username and password == valid_password:
    print("✅ Login successful!")
    print("   Welcome to the system!")

    # Additional features for logged-in users
    action = input("   What would you like to do? (view/edit/logout): ").lower()

    if action == "view":
        print("   📋 Displaying data...")
    elif action == "edit":
        print("   ✏️ Editing mode activated...")
    elif action == "logout":
        print("   👋 Logged out successfully!")
    else:
        print("   ❓ Unknown action. Defaulting to view mode.")

elif username == valid_username and password != valid_password:
    print("❌ Incorrect password!")
    print("   Username is correct, but password is wrong.")

elif username != valid_username and password == valid_password:
    print("❌ Incorrect username!")
    print("   Password is correct, but username is wrong.")

else:
    print("❌ Both username and password are incorrect!")
    print("   Please check your credentials.")

print("\n🔒 Session ended.")
