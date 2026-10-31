print("📖 Information Reader")

filename = "user_info.txt"

# Check if file exists first
import os
if os.path.exists(filename):
    print(f"📂 Reading from {filename}...")

    # Read the entire file
    with open(filename, 'r') as file:
        content = file.read()

    print("📋 File contents:")
    print("=" * 40)
    print(content)
    print("=" * 40)

    # Also read line by line
    print("\n📝 Reading line by line:")
    with open(filename, 'r') as file:
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

else:
    print(f"❌ File {filename} not found!")
    print("Run the save_to_file.py program first.")

# List all text files in directory
print(f"\n📁 All text files in current directory:")
for file in os.listdir('.'):
    if file.endswith('.txt'):
        file_size = os.path.getsize(file)
        print(f"   📄 {file} ({file_size} bytes)")
