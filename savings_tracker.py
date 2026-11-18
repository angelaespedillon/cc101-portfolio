total = 0
days = 0
amount = float(input("Savings today (0 to stop): "))
while amount != 0:
    total += amount
    days += 1
    amount = float(input("Savings today (0 to stop): "))

print(f"Total saved in {days} days: PHP {total :,.2f}")