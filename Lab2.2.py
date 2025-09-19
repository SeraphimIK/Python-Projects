# CISC 131 02
# Seraphim Ikuomola
# Lab 2 - Part 2.2

# This program asks the user for income information (W-2 wages,
# taxable interest, and ordinary dividends), computes total income,
# subtracts the standard deduction, and then calculates the federal
# income tax owed using a function.

# Function to compute the Federal Income Tax owed
def ComputeTax(adjustedIncome):
    # Multiply taxable income by 24% and subtract 6600 (IRS formula)
    taxOwed = (adjustedIncome * 0.24) - 6600
    return taxOwed

# --- Input Section ---
firstName = input("Please enter your first name: ")
wages = float(input("Enter total wages from W-2 forms: "))
interest = float(input("Enter taxable interest: "))
dividends = float(input("Enter ordinary dividends: "))

# --- Calculations ---
totalIncome = wages + interest + dividends             # Line 9
standardDeduction = 14600                              # 2024 standard deduction for single filers
taxableIncome = totalIncome - standardDeduction        # Line 15
taxOwed = ComputeTax(taxableIncome)                    # Call function

# --- Output Section ---
print("\n--- Federal Income Tax Results ---")
print("Name:", firstName)
print("Total Income (line 9):", totalIncome)
print("Taxable Income (line 15):", taxableIncome)
print("Federal Income Tax Owed:", taxOwed)