print("🎨 Advanced Formatting Showcase")

# Sample data
name = "John Doe"
salary = 75000
tax_rate = 0.22
hours_worked = 37.5
efficiency = 0.87

print("=" * 50)
print("EMPLOYEE REPORT")
print("=" * 50)

# Basic formatting
print(f"Employee: {name}")
print(f"Salary: ${salary}")

# Number formatting
print(f"Salary with commas: ${salary:,}")
print(f"Tax rate as percentage: {tax_rate:.1%}")
print(f"Hours (1 decimal): {hours_worked:.1f}")
print(f"Efficiency: {efficiency:.2%}")

# Alignment and padding
print(f"\nFormatted Table:")
print(f"{'Item':<20} {'Value':>10}")
print("-" * 30)
print(f"{'Name':<20} {name:>10}")
print(f"{'Salary':<20} {salary:>10,}")
print(f"{'Tax Rate':<20} {tax_rate:>10.1%}")

# Mathematical formatting
take_home = salary * (1 - tax_rate)
print(f"\n💰 Financial Summary:")
print(f"   Gross Salary: ${salary:>10,}")
print(f"   Tax Amount:   ${salary * tax_rate:>10,.2f}")
print(f"   Take Home:    ${take_home:>10,.2f}")

# Date and time formatting
from datetime import datetime
now = datetime.now()
print(f"\n📅 Report generated: {now:%Y-%m-%d %H:%M:%S}")
