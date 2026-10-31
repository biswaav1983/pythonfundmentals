print("💰 Personal Finance Advisor")

income = float(input("Enter your monthly income: $"))
expenses = float(input("Enter your monthly expenses: $"))

# Calculate savings
savings = income - expenses

print(f"\n📊 Financial Analysis:")
print(f"   Income: ${income:.2f}")
print(f"   Expenses: ${expenses:.2f}")
print(f"   Net Savings: ${savings:.2f}")

# Provide advice based on savings ratio
savings_ratio = (savings / income) * 100 if income > 0 else 0

if savings <= 0:
    print("\n⚠️ You're spending more than you earn!")
    print("   Immediate action needed:")
    print("   • Review and cut unnecessary expenses")
    print("   • Look for additional income sources")
elif savings_ratio < 10:
    print("\n🔸 You're saving less than 10% of your income.")
    print("   Suggestions:")
    print("   • Try to increase savings to at least 10%")
    print("   • Look for areas to reduce spending")
elif savings_ratio < 20:
    print("\n✅ Good job! You're saving 10-20% of your income.")
    print("   Keep it up and consider:")
    print("   • Building an emergency fund")
    print("   • Starting to invest for the future")
else:
    print("\n🌟 Excellent! You're saving 20%+ of your income!")
    print("   You're on track for financial success!")
    print("   Consider advanced strategies like investing")

print(f"\n💡 Savings Rate: {savings_ratio:.1f}%")
