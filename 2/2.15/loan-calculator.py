purchase_amount = input("Enter purchase amount: ")
interest_rate = input("Enter annual interest rate: ")
loan_duration = input("Loan duration (years): ")
down_payment = input("Include down payment? (y/n): ")
if down_payment == "y":
    down_payment = input("Enter down payment: ")
    loan_amount = int(purchase_amount) - int(down_payment)
# Loan monthly payment calculation
monthly_interest_rate = (int(interest_rate) / 100) / 12
numerator = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** (int(loan_duration) * 12)
denominator = (1 + monthly_interest_rate) ** (int(loan_duration) * 12) - 1
monthly_payment = round(numerator / denominator, 2)

print("\n----------------------\n")

print("Loan Details:")
print(f"\tPurchase amount: ${int(purchase_amount):,.2f}\n\tDown payment: ${int(down_payment):,.2f}\n\tLoan amount: ${int(loan_amount):,.2f}\n\tNumber of payments: {int(loan_duration) * 12} ({loan_duration} years)\n\tInterest rate: {interest_rate}%\n\tYears: {loan_duration}\n\tMonthly payment: ${float(monthly_payment):,.2f}")