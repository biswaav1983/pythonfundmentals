print("📝 String Processing Workshop")

# Get user text
text = input("Enter some text to analyze: ")

print(f"\n🔍 Analysis of: '{text}'")
print("=" * 50)

# Basic information
print(f"Length: {len(text)} characters")
print(f"Word count: {len(text.split())} words")

# Case information
print(f"Is all uppercase: {text.isupper()}")
print(f"Is all lowercase: {text.islower()}")
print(f"Is title case: {text.istitle()}")

# Content checks
print(f"Contains digits: {any(c.isdigit() for c in text)}")
print(f"Contains letters: {any(c.isalpha() for c in text)}")
print(f"Is alphanumeric: {text.isalnum()}")

# Transformations
print(f"\nTransformations:")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Title case: {text.title()}")
print(f"Reversed: {text[::-1]}")

# Find and replace
if ' ' in text:
    print(f"\nWord operations:")
    words = text.split()
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Words with underscores: {'_'.join(words)}")

# Character frequency
char_count = {}
for char in text.lower():
    if char.isalpha():
        char_count[char] = char_count.get(char, 0) + 1

if char_count:
    print(f"\n📊 Most common letters:")
    sorted_chars = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars[:5]:
        print(f"   '{char}': {count} times")
