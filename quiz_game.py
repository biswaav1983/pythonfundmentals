print("🧠 Python Knowledge Quiz")
print("Let's test what you've learned!")

score = 0
total_questions = 3

# Question 1
print("\n📝 Question 1:")
print("What function do you use to display text in Python?")
answer1 = input("Your answer: ").lower()

if answer1 == "print" or answer1 == "print()":
    print("✅ Correct! The print() function displays text.")
    score += 1
else:
    print("❌ Not quite. The answer is print().")

# Question 2
print("\n📝 Question 2:")
print("What function gets input from users?")
answer2 = input("Your answer: ").lower()

if answer2 == "input" or answer2 == "input()":
    print("✅ Excellent! The input() function gets user input.")
    score += 1
else:
    print("❌ Close! The answer is input().")

# Question 3
print("\n📝 Question 3:")
print("What do you put around text in Python? (just the symbol)")
answer3 = input("Your answer: ")

if answer3 == '"' or answer3 == "'" or answer3 == "quotes":
    print("✅ Perfect! Text goes in quotes.")
    score += 1
else:
    print('❌ Almost! Text goes in quotes ("text" or \'text\').')

# Show results
print("\n" + "🏆 " * 15)
print("QUIZ RESULTS")
print("🏆 " * 15)
print(f"Score: {score}/{total_questions}")

percentage = (score / total_questions) * 100
print(f"Percentage: {percentage:.1f}%")

if score == total_questions:
    print("🌟 Perfect score! You're a Python star!")
elif score >= 2:
    print("👍 Great job! You're learning well!")
elif score == 1:
    print("📚 Good start! Keep practicing!")
else:
    print("💪 Don't worry, everyone starts somewhere! Keep learning!")

print(f"\nThanks for taking the quiz! Keep coding! 💻")
