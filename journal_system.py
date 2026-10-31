print("📖 Personal Journal System")
import datetime
import os

journal_file = "my_journal.txt"

def add_journal_entry():
    """Add a new journal entry"""
    print("\n✏️ Adding a new journal entry:")

    # Get current date and time
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Get journal entry from user
    print(f"📅 Date: {date_str}")
    title = input("📝 Entry title: ")

    print("📖 Write your journal entry (type 'END' on a new line to finish):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)

    entry_text = '\n'.join(lines)

    # Format the journal entry
    journal_entry = f"""
{'='*50}
Date: {date_str}
Title: {title}
{'='*50}
{entry_text}
{'='*50}

"""

    # Append to journal file
    with open(journal_file, 'a') as file:
        file.write(journal_entry)

    print("✅ Journal entry saved!")

def read_journal():
    """Read and display all journal entries"""
    if os.path.exists(journal_file):
        print(f"\n📚 Reading your journal from {journal_file}:")
        with open(journal_file, 'r') as file:
            content = file.read()
            if content.strip():
                print(content)
            else:
                print("📝 Your journal is empty. Add some entries!")
    else:
        print("📝 No journal file found. Create your first entry!")

def journal_stats():
    """Show statistics about the journal"""
    if os.path.exists(journal_file):
        with open(journal_file, 'r') as file:
            content = file.read()

        lines = content.split('\n')
        words = content.split()
        entries = content.count('Date:')

        print(f"\n📊 Journal Statistics:")
        print(f"   Total entries: {entries}")
        print(f"   Total lines: {len(lines)}")
        print(f"   Total words: {len(words)}")
        print(f"   Total characters: {len(content)}")

        if entries > 0:
            avg_words = len(words) // entries
            print(f"   Average words per entry: {avg_words}")
    else:
        print("📝 No journal file found.")

# Main menu
while True:
    print("\n" + "📖" * 20)
    print("PERSONAL JOURNAL SYSTEM")
    print("📖" * 20)
    print("1. ✏️  Add new journal entry")
    print("2. 📚 Read all journal entries")
    print("3. 📊 Show journal statistics")
    print("4. 🚪 Exit")

    choice = input("\nChoose an option (1-4): ")

    if choice == '1':
        add_journal_entry()
    elif choice == '2':
        read_journal()
    elif choice == '3':
        journal_stats()
    elif choice == '4':
        print("👋 Goodbye! Happy journaling!")
        break
    else:
        print("❌ Invalid choice. Please choose 1-4.")
