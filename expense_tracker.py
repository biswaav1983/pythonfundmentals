print("💰 Personal Expense Tracker")

import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    """Load expenses from file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                return data.get('expenses', []), data.get('budget', 0)
        except:
            print("⚠️ Error loading data, starting fresh")
            return [], 0
    return [], 0

def save_expenses(expenses, budget):
    """Save expenses to file"""
    data = {
        'expenses': expenses,
        'budget': budget,
        'last_updated': datetime.now().isoformat()
    }
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=2)

def get_amount(prompt):
    """Get a valid monetary amount from user"""
    while True:
        try:
            amount = float(input(prompt))
            if amount >= 0:
                return round(amount, 2)
            else:
                print("❌ Amount must be positive")
        except ValueError:
            print("❌ Please enter a valid number")

def get_category():
    """Get expense category from user"""
    categories = [
        "Food & Dining", "Transportation", "Shopping", "Entertainment",
        "Bills & Utilities", "Healthcare", "Education", "Travel", "Other"
    ]

    print("\n📋 Choose a category:")
    for i, category in enumerate(categories, 1):
        print(f"   {i}. {category}")

    while True:
        try:
            choice = int(input("Enter category number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("❌ Invalid choice")
        except ValueError:
            print("❌ Please enter a number")

def add_expense(expenses):
    """Add a new expense"""
    print("\n💸 Adding New Expense")

    amount = get_amount("💵 Amount: $")
    description = input("📝 Description: ").strip()
    if not description:
        description = "No description"

    category = get_category()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': date
    }

    expenses.append(expense)
    print(f"✅ Added ${amount:.2f} expense for {category}")
    return expenses

def view_expenses(expenses):
    """Display all expenses"""
    if not expenses:
        print("\n📝 No expenses recorded yet")
        return

    print(f"\n📊 All Expenses ({len(expenses)} total)")
    print("=" * 80)
    print(f"{'Date':<20} {'Category':<15} {'Amount':<10} {'Description':<25}")
    print("-" * 80)

    total = 0
    for expense in expenses:
        date = expense['date'][:16]  # Show date and time
        category = expense['category'][:14]
        amount = f"${expense['amount']:.2f}"
        description = expense['description'][:24]

        print(f"{date:<20} {category:<15} {amount:<10} {description:<25}")
        total += expense['amount']

    print("-" * 80)
    print(f"{'TOTAL':<50} ${total:.2f}")

def expense_summary(expenses):
    """Show expense summary by category"""
    if not expenses:
        print("\n📝 No expenses to summarize")
        return

    # Group by category
    categories = {}
    total_spent = 0

    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        categories[category] = categories.get(category, 0) + amount
        total_spent += amount

    print(f"\n📊 Expense Summary")
    print("=" * 50)
    print(f"{'Category':<20} {'Amount':<12} {'Percentage':<10}")
    print("-" * 50)

    # Sort by amount (highest first)
    sorted_categories = sorted(categories.items(), key=lambda x: x[1], reverse=True)

    for category, amount in sorted_categories:
        percentage = (amount / total_spent) * 100 if total_spent > 0 else 0
        print(f"{category:<20} ${amount:<11.2f} {percentage:<9.1f}%")

    print("-" * 50)
    print(f"{'TOTAL':<20} ${total_spent:.2f} 100.0%")

def set_budget(current_budget):
    """Set monthly budget"""
    print(f"\n💰 Budget Management")
    if current_budget > 0:
        print(f"Current budget: ${current_budget:.2f}")

    new_budget = get_amount("Enter monthly budget: $")
    print(f"✅ Budget set to ${new_budget:.2f}")
    return new_budget

def budget_analysis(expenses, budget):
    """Analyze spending against budget"""
    if budget <= 0:
        print("\n⚠️ No budget set. Set a budget first to track progress.")
        return

    # Calculate current month spending
    current_month = datetime.now().strftime("%Y-%m")
    monthly_expenses = [
        exp for exp in expenses 
        if exp['date'].startswith(current_month)
    ]

    monthly_spent = sum(exp['amount'] for exp in monthly_expenses)
    remaining = budget - monthly_spent
    percentage_used = (monthly_spent / budget) * 100 if budget > 0 else 0

    print(f"\n📈 Budget Analysis for {current_month}")
    print("=" * 40)
    print(f"Monthly Budget:    ${budget:.2f}")
    print(f"Amount Spent:      ${monthly_spent:.2f}")
    print(f"Remaining:         ${remaining:.2f}")
    print(f"Budget Used:       {percentage_used:.1f}%")

    # Budget warnings
    if percentage_used >= 100:
        print("\n🚨 BUDGET EXCEEDED! You've spent more than your budget.")
    elif percentage_used >= 80:
        print("\n⚠️  WARNING: You've used 80%+ of your budget.")
    elif percentage_used >= 60:
        print("\n🔸 NOTICE: You've used over 60% of your budget.")
    else:
        print("\n✅ Good job! You're staying within budget.")

    # Daily spending average
    day_of_month = datetime.now().day
    if day_of_month > 0:
        daily_average = monthly_spent / day_of_month
        days_remaining = 30 - day_of_month  # Approximate
        projected_total = monthly_spent + (daily_average * days_remaining)

        print(f"\n📊 Projection:")
        print(f"Daily average:     ${daily_average:.2f}")
        print(f"Projected total:   ${projected_total:.2f}")

        if projected_total > budget:
            overage = projected_total - budget
            print(f"Projected overage: ${overage:.2f}")

def search_expenses(expenses):
    """Search expenses by description or category"""
    if not expenses:
        print("\n📝 No expenses to search")
        return

    search_term = input("\n🔍 Enter search term (description or category): ").lower()

    matching_expenses = [
        exp for exp in expenses
        if search_term in exp['description'].lower() or 
           search_term in exp['category'].lower()
    ]

    if matching_expenses:
        print(f"\n📋 Found {len(matching_expenses)} matching expenses:")
        print("-" * 60)
        total = 0
        for expense in matching_expenses:
            date = expense['date'][:10]
            print(f"{date} | {expense['category']:<15} | ${expense['amount']:.2f} | {expense['description']}")
            total += expense['amount']
        print("-" * 60)
        print(f"Total for matching expenses: ${total:.2f}")
    else:
        print(f"❌ No expenses found matching '{search_term}'")

# Main application
expenses, budget = load_expenses()

print("Welcome to your Personal Expense Tracker!")
print(f"💾 Data file: {DATA_FILE}")

while True:
    print("\n" + "💰" * 25)
    print("PERSONAL EXPENSE TRACKER")
    print("💰" * 25)
    print("1. 💸 Add New Expense")
    print("2. 📊 View All Expenses")
    print("3. 📈 Expense Summary")
    print("4. 💰 Set Monthly Budget")
    print("5. 📊 Budget Analysis")
    print("6. 🔍 Search Expenses")
    print("7. 💾 Save & Exit")

    choice = input("\nChoose option (1-7): ").strip()

    if choice == '1':
        expenses = add_expense(expenses)
        save_expenses(expenses, budget)
    elif choice == '2':
        view_expenses(expenses)
    elif choice == '3':
        expense_summary(expenses)
    elif choice == '4':
        budget = set_budget(budget)
        save_expenses(expenses, budget)
    elif choice == '5':
        budget_analysis(expenses, budget)
    elif choice == '6':
        search_expenses(expenses)
    elif choice == '7':
        save_expenses(expenses, budget)
        print("\n💾 Data saved successfully!")
        print("👋 Thank you for using Personal Expense Tracker!")
        break
    else:
        print("❌ Invalid choice. Please choose 1-7.")
