from finance_tools.tax import calculate_tax
from finance_tools.loan import calculate_emi

amount = float(input("Enter amount: "))
tax_rate = float(input("Enter tax rate: "))

print("Tax:", calculate_tax(amount, tax_rate))

p = float(input("Enter loan amount: "))
r = float(input("Enter interest rate: "))
y = int(input("Enter years: "))

print("EMI:", calculate_emi(p, r, y))