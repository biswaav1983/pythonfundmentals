print("💾 Information Saver")

# Get information from user
name = input("👤 Enter your name: ")
age = int(input("🎂 Enter your age: "))
hobby = input("🎯 Enter your favorite hobby: ")
city = input("🏙️ Enter your city: ")
date_saved = input("📅 Enter today's date: ")

# Create a message to save
message = f"""Personal Information:
Name: {name}
Age: {age}
Hobby: {hobby}
City: {city}
Date saved: {date_saved}
"""

# Write to file
filename = "user_info.txt"
with open(filename, 'w') as file:
    file.write(message)

print(f"\n✅ Information saved to {filename}!")
print("You can open this file with any text editor to see your data.")

# Let's also create a backup
backup_filename = f"{name.lower()}_backup.txt"
with open(backup_filename, 'w') as backup_file:
    backup_file.write(f"Backup for {name}\n" + message)

print(f"📋 Backup also created: {backup_filename}")
