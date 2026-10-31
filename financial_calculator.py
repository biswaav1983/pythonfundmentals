print("💰 Personal Finance Calculator")

# Get financial information
print("Let's calculate your financial health:")

monthly_income = float(input("💵 Monthly income: $"))
rent = float(input("🏠 Monthly rent/mortgage: $"))
groceries = float(input("🛒 Monthly groceries: $"))
utilities = float(input("⚡ Monthly utilities: $"))
transportation = float(input("🚗 Monthly transportation: $"))
entertainment = float(input("🎯 Monthly entertainment: $"))
other_expenses = float(input("📋 Other monthly expenses: $"))

# Calculate totals
total_expenses = rent + groceries + utilities + transportation + entertainment + other_expenses
monthly_savings = monthly_income - total_expenses
annual_income = monthly_income * 12
annual_savings = monthly_savings * 12

# Calculate percentages
if monthly_income > 0:
    savings_rate = (monthly_savings / monthly_income) * 100
    rent_percentage = (rent / monthly_income) * 100
else:
    savings_rate = 0
    rent_percentage = 0

# Display results
print("\n" + "💰" * 25)
print("FINANCIAL SUMMARY")
print("💰" * 25)

print(f"\n📊 Monthly Breakdown:")
print(f"{'Income:':<20} ${monthly_income:>10,.2f}")
print("-" * 32)
print(f"{'Rent/Mortgage:':<20} ${rent:>10,.2f}")
print(f"{'Groceries:':<20} ${groceries:>10,.2f}")
print(f"{'Utilities:':<20} ${utilities:>10,.2f}")
print(f"{'Transportation:':<20} ${transportation:>10,.2f}")
print(f"{'Entertainment:':<20} ${entertainment:>10,.2f}")
print(f"{'Other:':<20} ${other_expenses:>10,.2f}")
print("-" * 32)
print(f"{'Total Expenses:':<20} ${total_expenses:>10,.2f}")
print(f"{'Net Savings:':<20} ${monthly_savings:>10,.2f}")

print(f"\n📈 Annual Projections:")
print(f"{'Annual Income:':<20} ${annual_income:>12,.2f}")
print(f"{'Annual Savings:':<20} ${annual_savings:>12,.2f}")

print(f"\n📊 Financial Ratios:")
print(f"{'Savings Rate:':<20} {savings_rate:>11.1f}%")
print(f"{'Housing Ratio:':<20} {rent_percentage:>11.1f}%")

# Financial advice
print(f"\n💡 Financial Advice:")
if savings_rate >= 20:
    print("   🌟 Excellent! You're saving 20%+ of your income.")
elif savings_rate >= 10:
    print("   ✅ Good job! You're saving 10-20% of your income.")
elif savings_rate >= 5:
    print("   ⚠️ You're saving some money, but aim for 10%+.")
else:
    print("   🚨 Critical: You need to increase your savings rate!")

if rent_percentage > 30:
    print("   🏠 Your housing costs are high (>30% of income).")
elif rent_percentage > 25:
    print("   🏠 Your housing costs are moderate (25-30% of income).")
else:
    print("   🏠 Great! Your housing costs are reasonable (<25%).")

# Emergency fund calculation
emergency_fund_needed = total_expenses * 6
if monthly_savings > 0:
    months_to_emergency_fund = emergency_fund_needed / monthly_savings
    print(f"\n🆘 Emergency Fund Goal: ${emergency_fund_needed:,.2f}")
    print(f"   At current savings rate: {months_to_emergency_fund:.1f} months to build")
else:
    print(f"\n🆘 You need ${emergency_fund_needed:,.2f} for 6-month emergency fund")
    print("   Focus on reducing expenses to start saving!")
