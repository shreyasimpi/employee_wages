
name = input("Enter employee name: ")
wage = float(input("Enter daily wage: "))
days = int(input("Enter working days: "))

total_wages = (wage * days) + 200

print("\nEmployee Name:", name)
print("Daily Wage: Rs.", wage)
print("Working Days:", days)
print("Total Wages with Bonus: Rs.", total_wages)
