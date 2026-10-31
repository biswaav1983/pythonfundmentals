print("💰 Personal Finance Summary")

name = "John"
salary = 75000
expenses = 45000
savings = salary - expenses

# Using f-strings for neat formatting
print(f"Hello {name}!")
print(f"Annual salary: ${salary:,}")
print(f"Annual expenses: ${expenses:,}")
print(f"Annual savings: ${savings:,}")

# Calculate percentages
savings_rate = (savings / salary) * 100
print(f"Savings rate: {savings_rate:.1f}%")

# Create a nice summary
print(f"\n📊 {name}'s Financial Health:")
if savings_rate > 20:
    print(f"   Excellent! You're saving {savings_rate:.1f}% of your income!")
else:
    print(f"   You're saving {savings_rate:.1f}%. Consider increasing to 20%+")
