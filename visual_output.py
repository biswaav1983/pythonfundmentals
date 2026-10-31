print("=" * 40)
print("🏪 STORE RECEIPT")
print("=" * 40)

item1 = "Coffee"
price1 = 4.50

item2 = "Sandwich" 
price2 = 8.75

item3 = "Cookie"
price3 = 2.25

total = price1 + price2 + price3
tax = total * 0.08
final_total = total + tax

print(f"☕ {item1:<20} ${price1:>6.2f}")
print(f"🥪 {item2:<20} ${price2:>6.2f}")
print(f"🍪 {item3:<20} ${price3:>6.2f}")
print("-" * 30)
print(f"   Subtotal:        ${total:>6.2f}")
print(f"   Tax (8%):        ${tax:>6.2f}")
print("=" * 30)
print(f"   TOTAL:           ${final_total:>6.2f}")
print("=" * 40)
print("Thank you for your purchase! 😊")
