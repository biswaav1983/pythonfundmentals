print("🛡️ Safe File Operations Demo")

import os
import shutil
from datetime import datetime

def safe_write_file(filename, content):
    """Safely write to a file with backup"""
    try:
        # Create backup if file exists
        if os.path.exists(filename):
            backup_name = f"{filename}.backup"
            shutil.copy2(filename, backup_name)
            print(f"📋 Backup created: {backup_name}")

        # Write the new content
        with open(filename, 'w') as file:
            file.write(content)

        print(f"✅ Successfully wrote to {filename}")
        return True

    except PermissionError:
        print(f"❌ Permission denied: Cannot write to {filename}")
        return False
    except Exception as e:
        print(f"❌ Error writing file: {e}")
        return False

def safe_read_file(filename):
    """Safely read from a file"""
    try:
        if not os.path.exists(filename):
            print(f"❌ File {filename} does not exist")
            return None

        with open(filename, 'r') as file:
            content = file.read()

        print(f"✅ Successfully read {filename}")
        return content

    except PermissionError:
        print(f"❌ Permission denied: Cannot read {filename}")
        return None
    except UnicodeDecodeError:
        print(f"❌ Cannot decode {filename} - might be a binary file")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def get_file_info(filename):
    """Get detailed information about a file"""
    if os.path.exists(filename):
        stat = os.stat(filename)

        print(f"\n📊 File Information: {filename}")
        print("-" * 40)
        print(f"Size: {stat.st_size} bytes")
        print(f"Created: {datetime.fromtimestamp(stat.st_ctime)}")
        print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")
        print(f"Readable: {os.access(filename, os.R_OK)}")
        print(f"Writable: {os.access(filename, os.W_OK)}")
    else:
        print(f"❌ File {filename} does not exist")

# Demo the safe operations
print("Let's test safe file operations!")

# Get filename from user
filename = input("📝 Enter a filename to work with: ")

# Get content to write
print("📖 Enter content to write (type 'END' on new line to finish):")
lines = []
while True:
    line = input()
    if line.strip().upper() == 'END':
        break
    lines.append(line)

content = '\n'.join(lines)

# Add timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
content_with_timestamp = f"Created: {timestamp}\n\n{content}"

# Safely write the file
print(f"\n💾 Writing to {filename}...")
if safe_write_file(filename, content_with_timestamp):

    # Show file information
    get_file_info(filename)

    # Read it back
    print(f"\n📖 Reading back from {filename}...")
    read_content = safe_read_file(filename)

    if read_content:
        print("\n📋 File contents:")
        print("=" * 40)
        print(read_content)
        print("=" * 40)

print("\n🎯 Safe file operations completed!")

# List all files in current directory
print("\n📁 Files in current directory:")
for file in os.listdir('.'):
    if os.path.isfile(file):
        size = os.path.getsize(file)
        print(f"   📄 {file} ({size} bytes)")
