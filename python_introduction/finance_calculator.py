monthly_expense = int(input("What's your monthly expense? "))
monthly_income = int(input("What's your monthly income? "))

monthly_savings = monthly_expense - monthly_income

projected_savings = int( monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
