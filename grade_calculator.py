print("📊 Grade Calculator")

score = float(input("Enter your test score (0-100): "))

if score >= 90:
    print("🏆 Excellent! You got an A!")
    print("   Outstanding work!")
elif score >= 80:
    print("⭐ Great job! You got a B!")
    print("   Very good work!")
elif score >= 70:
    print("👍 Good work! You got a C!")
    print("   You're doing well!")
elif score >= 60:
    print("📚 You got a D. Keep studying!")
    print("   You can improve!")
else:
    print("😔 You got an F. Don't give up!")
    print("   Study harder next time!")

print(f"\n💯 Your score: {score}")
